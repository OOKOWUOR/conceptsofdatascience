# plot_results.py

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def make_plot(
    df: pd.DataFrame, x: str, y: str, title: str, outpath: Path
) -> None:
    plt.figure(figsize=(8, 5))

    for dataset in sorted(df["dataset"].unique()):
        subset: pd.DataFrame = df[df["dataset"] == dataset]
        plt.plot(subset[x], subset[y], marker="o", label=dataset)

    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


if __name__ == "__main__":
    HERE = Path(__file__).resolve()
    PROJECT_ROOT = HERE.parent.parent

    data = pd.read_csv(PROJECT_ROOT / "results/benchmark_results.csv")

    make_plot(
        data,
        "n_inserted",
        "insert_time_sec",
        "Insertion time vs inserted items",
        PROJECT_ROOT / "results/insert_time.png",
    )

    make_plot(
        data,
        "n_inserted",
        "present_search_time_sec",
        "Lookup time (present) vs inserted items",
        PROJECT_ROOT / "results/search_present_time.png",
    )

    make_plot(
        data,
        "n_inserted",
        "absent_search_time_sec",
        "Lookup time (absent) vs inserted items",
        PROJECT_ROOT / "results/search_absent_time.png",
    )

    make_plot(
        data,
        "n_inserted",
        "observed_false_positive_rate",
        "Observed false positive rate vs inserted items",
        PROJECT_ROOT / "results/observed_fpr.png",
    )

    make_plot(
        data,
        "n_inserted",
        "theoretical_false_positive_rate",
        "Theoretical false positive rate vs inserted items",
        PROJECT_ROOT / "results/theoretical_fpr.png",
    )

    make_plot(
        data,
        "n_inserted",
        "bits_per_item",
        "Bits per item vs inserted items",
        PROJECT_ROOT / "results/bits_per_item.png",
    )

    print("Plots saved in results/.")
