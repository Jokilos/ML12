import os
import re
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import Dataset, load_dataset as hf_load_dataset
from typing import List, Tuple
from tqdm import tqdm
import argparse

os.environ["TOKENIZERS_PARALLELISM"] = "false"

class ThinkEvaluator:
    """
    Evaluator for <think>-mode reasoning with a fixed token budget.

    Phase 1: Generate up to `budget` tokens inside the <think> tag,
             blocking premature </think> to force full-length reasoning.
    Phase 2: Append </think> and "Final answer:" and generate a short answer,
             then extract the first number as the model's answer.
    """
    def __init__(self, model_name: str, dataset: Dataset, device: str):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
        self.dataset = dataset

    def format_prompt(self, question: str) -> str:
        text = (
            "<|im_start|>user\n"
            f"Question: {question}"
            "<|im_end|>\n"
            "<|im_start|>assistant\n"
            "<think>"
        )
        return text

    def evaluate_with_budget(self, budgets: List[int], batch_size: int, verbose: bool = True) -> float:
        """
        Evaluate the model on all questions using the given token budget.
        Returns the accuracy.
        """
        mx_budget = max(budgets)
        correct = {
            b: 0
            for b in budgets
        }
        total   = len(self.dataset)

        # Prepare IDs for blocking the closing tag
        bad_ids = self.tokenizer(
            ["</think>", "<|im_start|>", "<think>", "<|im_end|>", "<|endoftext|>", "<tool_call>", "<tool_response>"],
            add_special_tokens=False
        ).input_ids

        loader = torch.utils.data.DataLoader(self.dataset, batch_size=batch_size, num_workers=1)
        for batch in tqdm(loader):
            # Phase 1: reasoning generation
            prompts = [self.format_prompt(q) for q in batch["question"]]
            inputs = self.tokenizer(prompts, padding=True, return_tensors="pt").to(self.device)
            with torch.no_grad():
                reasoning_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=mx_budget,
                    pad_token_id=self.tokenizer.eos_token_id,
                    do_sample=False,
                    bad_words_ids=bad_ids,
                    use_cache=True,
                    eos_token_id=None,
                )
            reasonings = [
                r.replace('<|endoftext|>', '') for r in self.tokenizer.batch_decode(reasoning_ids, skip_special_tokens=False)
            ]

            enc2 = self.tokenizer(reasonings, padding=True, return_tensors="pt").to(self.device)

            final_answer_tokens = self.tokenizer(["\n</think>\n\nFinal answer (a single number): "], return_tensors="pt").to(self.device).input_ids

            for budget in budgets:
                budget_diff = mx_budget - budget
                cot_len = enc2.input_ids.shape[1] - budget_diff
                seq_len = cot_len + final_answer_tokens.shape[1]

                new_input_ids = torch.zeros((enc2.input_ids.shape[0], seq_len), dtype=enc2.input_ids.dtype, device=self.device)
                new_attention_mask = torch.ones_like(new_input_ids)

                new_input_ids[:, :cot_len] = enc2.input_ids[:, :cot_len]
                new_attention_mask[:, :cot_len] = enc2.attention_mask[:, :cot_len]
                new_input_ids[:, cot_len:] = final_answer_tokens

                with torch.no_grad():
                    ans_out = self.model.generate(
                        input_ids = new_input_ids,
                        attention_mask = new_attention_mask,
                        max_new_tokens=16,
                        pad_token_id=self.tokenizer.eos_token_id,
                        do_sample=False
                    )

                final_texts = self.tokenizer.batch_decode(ans_out[:, new_input_ids.shape[1]:], skip_special_tokens=True)

                followups = self.tokenizer.batch_decode(new_input_ids, skip_special_tokens=False)

                for final_text, answer, followup in zip(final_texts, batch["answer"], followups, strict=True):
                # Extract first integer from the final text
                    m = re.search(r"\d+", final_text)
                    pred = m.group(0) if m else final_text.strip()

                    hit = pred == str(answer).strip()
                    correct[budget] += int(hit)

                    if verbose:
                        print(f"============{budget}============\n{followup}{final_text.strip()}")
                        print(f"\n\nExtracted answer: {pred} (expected {answer}) -> {'✔' if hit else '✘'}\n\n\n")

        return {
            b: correct[b] / total if total else 0.0 for b in budgets
        }

def load_dataset(name: str,
                 split: str = "test",
                 question_column: str = "question_concat",
                 answer_column: str = "Answer"):
    ds = (
        hf_load_dataset(name, split=split)
        .select_columns([question_column, answer_column])
        .rename_columns({question_column: "question", answer_column: "answer"})
    )

    def add_length(batch):
        return {"length": [len(t) for t in batch["question"]]}

    ds = ds.map(add_length, batched=True, batch_size=1000)
    ds = ds.sort("length")
    ds = ds.remove_columns("length")

    return ds

if __name__ == "__main__":
    transformers.logging.set_verbosity_error()

    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda", help="Device to use.")
    parser.add_argument("--model_name", help="Model name.", required=True)
    parser.add_argument("--dataset_name", default="ChilleD/SVAMP", help="Dataset name.")
    parser.add_argument("--question_column", default="question_concat", help="Column with question.")
    parser.add_argument("--answer_column", default="Answer", help="Column with answer.")
    parser.add_argument("--batch_size", default=4, type=int, help="Batch sizes.")
    parser.add_argument("--budgets", default=[25,50,100,200,400,800], help="Budgets.")
    parser.add_argument("--verbose", default=False, help="Verbose.")
    args = parser.parse_args()

    dataset = load_dataset(
        name=args.dataset_name,
        split="test",
        question_column=args.question_column,
        answer_column=args.answer_column
    )

    evaluator = ThinkEvaluator(args.model_name, dataset, device=args.device)
    results = evaluator.evaluate_with_budget(args.budgets, args.batch_size, verbose=args.verbose)

    print("Summary of results:")
    for b, acc in results.items():
        print(f"  {b} tokens → {acc:.2%}")
