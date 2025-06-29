import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class ExperimentResults:
    plot_name: str
    qwen2_baseline_acc: float
    qwen3_baseline_acc: float
    thinking_budgets: list[int]
    qwen2_wait_acc: list[float]
    qwen3_wait_acc: list[float]
    qwen3_think_acc: list[float]

    def __post_init__(self):
        assert (
            self.qwen3_wait_acc[0] ==
            self.qwen3_think_acc[0] ==
            self.qwen3_baseline_acc
        )
        assert self.qwen2_wait_acc[0] == self.qwen2_baseline_acc
        assert (
            len(self.thinking_budgets) ==
            len(self.qwen2_wait_acc) ==
            len(self.qwen3_think_acc) ==
            len(self.qwen3_think_acc)
        )

    @classmethod
    def for_svamp(cls) -> "ExperimentResults":
        results = cls(
            plot_name = "svamp",
            qwen2_baseline_acc = 5.3, # TODO fill
            qwen3_baseline_acc = 15.1, # TODO fill
            thinking_budgets = [0, 100, 200, 300, 400], # TODO fill
            qwen2_wait_acc = [5.3, 10, 12, 15, 20], # TODO fill
            qwen3_wait_acc = [15.1, 18, 23, 28, 33], # TODO fill
            qwen3_think_acc = [15.1, 55, 56, 66, 74], # TODO fill
        )
        return results


def plot_results(results: ExperimentResults):
    qwen2_color = "blue"
    qwen3_color = "green"

    plt.figure(figsize=(8, 6))

    # Baselines.
    plt.axhline(
        y=results.qwen2_baseline_acc, color=qwen2_color,
        linestyle="dotted", linewidth=2,
        label="Qwen2.5 (baseline)"
    )
    plt.axhline(
        y=results.qwen3_baseline_acc, color=qwen3_color,
        linestyle="dotted", linewidth=2,
        label="Qwen3 (baseline)"
    )

    # Thinking with "Wait".
    plt.plot(
        results.thinking_budgets, results.qwen2_wait_acc,
        marker="s", linestyle="-.", color=qwen2_color,
        label="Qwen2.5 (Wait)"
    )
    plt.plot(
        results.thinking_budgets, results.qwen3_wait_acc,
        marker="s", linestyle="-.", color=qwen3_color,
        label="Qwen3 (Wait)"
    )

    # Thinking with "<think>".
    plt.plot(
        results.thinking_budgets, results.qwen3_think_acc,
        marker="^", linestyle="-", color=qwen3_color,
        label="Qwen3 (<think>)"
    )

    plt.xlabel("Thinking budget (tokens)")
    plt.ylabel("Accuracy (%)")
    plt.title("Accuracy vs. Thinking Budget")
    plt.legend()
    plt.grid()
    plt.tight_layout()

    plt.savefig(f"../report/{results.plot_name}.svg")


if __name__ == "__main__":
    plot_results(ExperimentResults.for_svamp())
