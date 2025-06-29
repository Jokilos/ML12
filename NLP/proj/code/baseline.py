from datasets import load_dataset
import re
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm
import argparse


def run_baseline(
    model_name: str,
    device: str,
    dataset_name: str = "ChilleD/SVAMP",
    question_column: str = "question_concat",
    answer_column: str = "Answer",
    batch_size: int = 8,
) -> float:
    # Dataset.
    ds = load_dataset(dataset_name, split="test")

    # Sort by length.
    def add_length(batch):
        return {"length": [len(t) for t in batch[question_column]]}
    ds = ds.map(add_length, batched=True, batch_size=1000, keep_in_memory=True)
    ds = ds.sort("length")
    ds = ds.remove_columns("length")

    loader = torch.utils.data.DataLoader(ds, batch_size=batch_size, num_workers=1)

    # Tokenizer and model.
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

    correct = total = 0
    for batch in tqdm(loader):
        prompts = [
            f"<|im_start|>user\nQuestion: {q}\n<|im_end|>\n<|im_start|>assistant\n{'<think>\n\n</think>\n\n' if model_name.startswith('Qwen/Qwen3') else ''}Final answer (a single number): "
            for q in batch[question_column]
        ]
        inputs = tokenizer(prompts, padding=True, return_tensors="pt").to(device)

        outputs = model.generate(**inputs, max_new_tokens=15, do_sample=False)
        preds = tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

        # Count correct predictions.
        for pred, answer in zip(preds, batch[answer_column], strict=True):
            m = re.search(r"\d+", pred) # Find the first number in the output.
            if m and m.group() == answer:
                correct += 1
            total += 1

    return correct / total


if __name__ == "__main__":
    transformers.logging.set_verbosity_error()

    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda", help="Device to use.")
    parser.add_argument("--model_name", help="Model name.", required=True)
    parser.add_argument("--dataset_name", default="ChilleD/SVAMP", help="Dataset name.")
    parser.add_argument("--question_column", default="question_concat", help="Column with question.")
    parser.add_argument("--answer_column", default="Answer", help="Column with answer.")
    parser.add_argument("--batch_size", default=8, help="Batch size.")
    args = parser.parse_args()

    result = run_baseline(**args.__dict__)

    print(f"ACCURACY FOR '{args.dataset_name}' USING '{args.model_name}':")
    print(result)
