# plot_results.py
"""Utility script to generate plots from benchmark results."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def make_plot(
    df: pd.DataFrame, x: str, y: str, title: str, outpath: Path
) -> None:
    """Generate and save a line plot for a given dataset and metrics."""
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


def plot_averages(
    df: pd.DataFrame, x: str, y: str, title: str, outPath: Path
) -> None:
    """Generate and save a line plot of average values."""
    avg = "avg_" + y
    df[avg] = df[y] / df[x]
    make_plot(df, x, avg, title, outPath)


def plot_totals(
    df: pd.DataFrame, x: str, y: str, title: str, outPath: Path
) -> None:
    """Generate and save a line plot of total values from averages."""
    if y == "bits_per_item":
        tot = "total_storage (bits)"
    else:
        tot = "total_of_" + y
    df[tot] = df[y] * df[x]
    make_plot(df, x, tot, title, outPath)


if __name__ == "__main__":
    here = Path(__file__).resolve()
    project_root = here.parent.parent

    data = pd.read_csv(project_root / "results/benchmark_results.csv")

    make_plot(
        data,
        "n_inserted",
        "insert_time_sec",
        "Total insertion time (sec) vs inserted items",
        project_root / "results/total_insert_time.png",
    )

    plot_averages(
        data,
        "n_inserted",
        "insert_time_sec",
        "Average insertion time (sec) vs inserted items",
        project_root / "results/avg_insert_time.png",
    )

    make_plot(
        data,
        "n_inserted",
        "present_search_time_sec",
        "Total lookup time (present) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/total_search_present_time.png",
    )

    plot_averages(
        data,
        "n_inserted",
        "present_search_time_sec",
        "Average lookup time (present) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/avg_search_present_time.png",
    )

    make_plot(
        data,
        "n_inserted",
        "absent_search_time_sec",
        "Total lookup time (absent) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/total_search_absent_time.png",
    )

    plot_averages(
        data,
        "n_inserted",
        "absent_search_time_sec",
        "Average lookup time (absent) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/avg_search_absent_time.png",
    )

    make_plot(
        data,
        "n_inserted",
        "false_negatives",
        "Observed false negatives vs inserted items",
        project_root / "results/observed_fneg.png",
    )

    make_plot(
        data,
        "n_inserted",
        "observed_false_positive_rate",
        "Observed false positive rate vs inserted items",
        project_root / "results/observed_fpr.png",
    )

    make_plot(
        data,
        "n_inserted",
        "theoretical_false_positive_rate",
        "Theoretical false positive rate vs inserted items",
        project_root / "results/theoretical_fpr.png",
    )

    make_plot(
        data,
        "n_inserted",
        "bits_per_item",
        "Average used bits per item vs inserted items",
        project_root / "results/used_bits_per_item.png",
    )

    plot_totals(
        data,
        "n_inserted",
        "bits_per_item",
        "Total storage in bits vs inserted items",
        project_root / "results/total_storage.png",
    )

    print("Plots saved in results/.")
