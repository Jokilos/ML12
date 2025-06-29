from datasets import load_dataset
import re
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteriaList, StopStringCriteria, StoppingCriteria, EosTokenCriteria
from tqdm import tqdm
import argparse
from functools import reduce


class CustomCriteria(StoppingCriteria):
    def __init__(self, inner, batch_size, device):
        self.inner = inner
        self.markers = torch.zeros(batch_size, device=device, dtype=torch.bool)
        self.generated_counter = torch.zeros(batch_size, device=device, dtype=torch.long)

    def __call__(self, input_ids, scores, **kwargs):
        results = reduce(torch.logical_or, [c(input_ids, scores, **kwargs) for c in self.inner])
        self.generated_counter += torch.logical_not(self.markers)
        self.markers[...] = torch.logical_or(results, self.markers)
        if self.markers.all():
            return self.markers
        return torch.zeros_like(self.markers)


def remove_assistant_end(s: str):
    idx_assistant_begin = s.find("<|im_start|>assistant")
    if (idx_assistant_begin == -1):
        return s
    bad_strings = ["Question:", "<|im_end|>"]
    locations = [
        s.find(bs, idx_assistant_begin) for bs in bad_strings
    ]
    locations = [
        l for l in locations if l != -1
    ]
    if len(locations) == 0:
        return s
    idx_assistant_end = min(locations)
    new_s = s[:idx_assistant_end]
    if new_s.endswith('\n'):
        return new_s[:-1]
    return new_s


def process_model_outputs(outputs, tokenizer, starting_length, generated_lengths, budgets, ids, eos_id):
    B = budgets.shape[0]
    capped_generated_lengths = torch.minimum(budgets, generated_lengths)
    allowed_lengths = (starting_length + capped_generated_lengths).long() 

    for i in range(B):
        outputs[i, allowed_lengths[i]:] = eos_id

    capped_generated_lengths = torch.minimum(budgets, generated_lengths)
    texts = tokenizer.batch_decode(outputs, skip_special_tokens=False)
    bare_texts = [remove_assistant_end(s.replace('<|endoftext|>', '')) for s in texts]
    budgets_left = budgets - capped_generated_lengths
    remain_prompts = []
    remain_ids = []
    remain_budgets = []
    new_outputs = []

    for i in range(B):
        if budgets_left[i] < 5:
            new_outputs.append((ids[i], bare_texts[i]))
        else:
            remain_prompts.append(bare_texts[i]+"\nWait, ")
            remain_ids.append(ids[i])
            remain_budgets.append(budgets_left[i])
    return new_outputs, remain_prompts, remain_ids, remain_budgets


def eval_with_thinking_budget(
        model,
        tokenizer,
        device,
        loader,
        question_column,
        answer_column,
        budget_set,
        logdir,
        additional_cot = ''
) :
    if logdir is not None:
        with open(logdir, 'a+', encoding='utf8') as f:
            f.write(f"=======================\nThinking budgets {budget_set}\n=======================\n\n\n\n")
    
    eos_id = tokenizer.eos_token_id
    end_id = tokenizer.get_vocab()["<|im_end|>"]

    total = 0
    mx_budget = max(budget_set)
    correct = {
        b: 0
        for b in budget_set
    }

    for i, batch in enumerate(tqdm(loader, f"Budget: {mx_budget}")):
        prompts = [f"<|im_start|>user\nQuestion: {q}\n<|im_end|>\n<|im_start|>assistant\n{additional_cot}Let's think step by step. " for q in batch[question_column]]
        total += len(prompts)

        budgets = [mx_budget for _ in prompts]
        ids = [i for i in range(len(prompts))]
        thoughts = []        

        while len(budgets) > 0:
            inputs = tokenizer(prompts, padding=True, return_tensors="pt").to(device)
            start_length = inputs.input_ids.shape[1]
            budget_tensor = torch.Tensor(budgets).to(device)
            criterion = CustomCriteria([EosTokenCriteria([eos_id, end_id]), StopStringCriteria(tokenizer, "Question:")], len(prompts), device)
            criteria = StoppingCriteriaList([
                criterion
            ])
            outputs = model.generate(**inputs, max_new_tokens=budget_tensor.max()+1, stopping_criteria=criteria, do_sample=False, use_cache=True)
            new_thoughts, prompts, ids, budgets = process_model_outputs(outputs, tokenizer, start_length, criterion.generated_counter, budget_tensor, ids, eos_id)
            thoughts.extend(new_thoughts)

        thoughts.sort(key=lambda x: x[0])

        cot_tokens = tokenizer([t for _, t in thoughts], padding=True, return_tensors="pt").to(device)

        final_answer_tokens = tokenizer(["\nFinal answer (a single number): "], return_tensors="pt").to(device).input_ids

        for budget in budget_set:
            budget_diff = mx_budget - budget
            cot_len = cot_tokens.input_ids.shape[1] - budget_diff
            seq_len = cot_len + final_answer_tokens.shape[1]

            new_input_ids = torch.zeros((cot_tokens.input_ids.shape[0], seq_len), dtype=cot_tokens.input_ids.dtype, device=device)
            new_attention_mask = torch.ones_like(new_input_ids)

            new_input_ids[:, :cot_len] = cot_tokens.input_ids[:, :cot_len]
            new_attention_mask[:, :cot_len] = cot_tokens.attention_mask[:, :cot_len]
            new_input_ids[:, cot_len:] = final_answer_tokens

            outputs = model.generate(
                input_ids=new_input_ids, 
                attention_mask=new_attention_mask, 
                max_new_tokens=15, 
                do_sample=False, 
                use_cache=True
            )

            preds = tokenizer.batch_decode(outputs[:, new_input_ids.shape[1]:], skip_special_tokens=False)
            preds = [p.replace('<|endoftext|>', '') for p in preds]

            for pred, answer in zip(preds, batch[answer_column], strict=True):
                    m = re.search(r"\d+", pred) # Find the first number in the output.
                    if m and m.group() == answer:
                        correct[budget] += 1

            if i % 4 == 0 and logdir is not None:
                thought = tokenizer.decode(new_input_ids[0], skip_special_tokens=False).replace('<|endoftext|>', '')
                with open(logdir, 'a+', encoding='utf8') as f:
                    f.write(f"+++++++{budget}++++++++\n{thought}{preds[0]}\n+++++++++++++++\nCorrect answer: {batch[answer_column][0]}\n+++++++++++++++\n\n")
                
    return [
        (budget, correct[budget] / total)
        for budget in budget_set
    ]


def run_natural_prompts(
    model_name: str,
    device: str,
    dataset_name: str = "ChilleD/SVAMP",
    question_column: str = "question_concat",
    answer_column: str = "Answer",
    batch_size: int = 8,
    num_budgets: int = 1,
    budget_start: int = 50,
    logdir = None
) -> float:
    # Dataset.
    ds = load_dataset(dataset_name, split="test")

    def add_length(batch):
        return {"length": [len(t) for t in batch[question_column]]}

    ds = ds.map(add_length, batched=True, batch_size=1000)
    ds = ds.sort("length")
    ds = ds.remove_columns("length")

    loader = torch.utils.data.DataLoader(ds, batch_size=batch_size, num_workers=1)

    # Tokenizer and model.
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

    if logdir is not None:
        with open(logdir, 'w+', encoding='utf8') as f:
            f.write(f"Model: {model_name}\nDataset: {dataset_name}\n\n\n")

    budget_set = [
        int(budget_start * (2 ** i))
        for i in range(num_budgets)
    ]

    acc = eval_with_thinking_budget(
        model,
        tokenizer,
        device,
        loader,
        question_column,
        answer_column,
        budget_set,
        logdir,
        '<think>\n\n</think>\n\n' if model_name.startswith('Qwen/Qwen3') else ''
    )

    return acc


if __name__ == "__main__":
    transformers.logging.set_verbosity_error()

    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda", help="Device to use.")
    parser.add_argument("--model_name", help="Model name.", required=True)
    parser.add_argument("--dataset_name", default="ChilleD/SVAMP", help="Dataset name.")
    parser.add_argument("--question_column", default="question_concat", help="Column with question.")
    parser.add_argument("--answer_column", default="Answer", help="Column with answer.")
    parser.add_argument("--batch_size", default=8, type=int, help="Batch size.")
    parser.add_argument("--logdir", help="Directory for model output logs.")
    parser.add_argument("--num_budgets", default=1, type=int, help="The number of different thinking budgets to evaluate")
    parser.add_argument("--budget_start", default=50, type=int, help="The lowest thinking budget to evaluate")
    args = parser.parse_args()

    results = run_natural_prompts(**args.__dict__)

    budgets, accuracies = zip(*results)

    print(f"FOR '{args.dataset_name}' USING '{args.model_name}':")
    print(f"BUDGETS: {budgets}")
    print(f"ACCURACIES: {accuracies}")
