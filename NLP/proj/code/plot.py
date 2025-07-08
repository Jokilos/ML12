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
        self.qwen2_wait_acc = [self.qwen2_baseline_acc] + self.qwen2_wait_acc
        self.qwen3_wait_acc = [self.qwen3_baseline_acc] + self.qwen3_wait_acc
        self.qwen3_think_acc = [self.qwen3_baseline_acc] + self.qwen3_think_acc

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
        ), (
            len(self.thinking_budgets), 
            len(self.qwen2_wait_acc),
            len(self.qwen3_think_acc),
            len(self.qwen3_think_acc)
        )

    @classmethod
    def for_gsm(cls) -> "ExperimentResults":
        results = cls(
            plot_name = "gsm8k",
            qwen2_baseline_acc = 0.0606,  # Qwen2.5-0.5B-Instruct
            qwen3_baseline_acc = 0.0379,  # Qwen3-0.6B

            thinking_budgets = [0, 25, 50, 100, 200, 400, 800],

            qwen2_wait_acc = [
                0.0303,  # 25 tokens
                0.0417,  # 50
                0.0970,  # 100
                0.2669,  # 200
                0.2987,  # 400
                0.3252   # 800
            ],

            qwen3_wait_acc = [
                0.0804,  # 25
                0.1736,  # 50
                0.3442,  # 100
                0.5087,  # 200
                0.5550,  # 400
                0.5625   # 800
            ],

            qwen3_think_acc = [
                0.0447,  # 25
                0.0371,  # 50
                0.0432,  # 100
                0.1221,  # 200
                0.4905,  # 400
                0.6657   # 800
            ],
        )

        return results

    @classmethod
    def for_svamp(cls) -> "ExperimentResults":
        results = cls(
            plot_name = "svamp",

            qwen2_baseline_acc = 0.2633,  # Qwen2.5-0.5B-Instruct
            qwen3_baseline_acc = 0.1000,  # Qwen3-0.6B

            thinking_budgets = [0, 25, 50, 100, 200, 400, 800],

            qwen2_wait_acc = [
                0.2133,  # 25
                0.2667,  # 50
                0.4033,  # 100
                0.4000,  # 200
                0.4600,  # 400
                0.4700   # 800
            ],

            qwen3_wait_acc = [
                0.5367,  # 25
                0.6467,  # 50
                0.7400,  # 100
                0.7533,  # 200
                0.7600,  # 400
                0.7600   # 800
            ],

            qwen3_think_acc = [
                0.1800,  # 25
                0.1567,  # 50
                0.1833,  # 100
                0.4700,  # 200
                0.7400,  # 400
                0.8033   # 800
            ],
        )

        return results

def plot_results(results: ExperimentResults):
    qwen2_color = "blue"
    qwen3_color = "green"

    plt.figure(figsize=(4, 3))

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
    plot_results(ExperimentResults.for_gsm())
