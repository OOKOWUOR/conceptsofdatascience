# plot_results.py
"""Utility script to generate plots from benchmark results."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_plot(
    df: pd.DataFrame, x: str, y: str, title: str, out_path: Path
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
    plt.savefig(out_path)
    plt.close()


def plot_averages(
    df: pd.DataFrame, x: str, y: str, title: str, out_path: Path
) -> None:
    """Generate and save a line plot of average values."""
    avg = "avg_" + y
    df[avg] = df[y] / df[x]
    make_plot(df, x, avg, title, out_path)


def plot_totals(
    df: pd.DataFrame, x: str, y: str, title: str, out_path: Path
) -> None:
    """Generate and save a line plot of total values from averages."""
    if y == "bits_per_item":
        tot = "total_storage (bits)"
    else:
        tot = "total_of_" + y
    df[tot] = df[y] * df[x]
    make_plot(df, x, tot, title, out_path)


def plot_compressions(
    df: pd.DataFrame, x: str, y: str, title: str, out_path: Path, label: str
) -> None:
    """Generate and save line plots for compression analysis."""
    plot = sns.relplot(data=df, x=x, y=y, col="dataset", hue=label)
    plot.fig.suptitle(title)
    plot.fig.subplots_adjust(top=0.9)
    plt.savefig(out_path)
    plt.close()


if __name__ == "__main__":
    here = Path(__file__).resolve()
    project_root = here.parent.parent

    data = pd.read_csv(project_root / "results/benchmark_results.csv")
    exp_items = pd.read_csv(
        project_root / "results/benchmark_expected_items.csv"
    )
    exp_fpr = pd.read_csv(project_root / "results/benchmark_expected_fpr.csv")

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
        "Compression rate: average used bits per item vs inserted items",
        project_root / "results/used_bits_per_item.png",
    )

    plot_totals(
        data,
        "n_inserted",
        "bits_per_item",
        "Total storage in bits vs inserted items",
        project_root / "results/total_storage.png",
    )

    plot_compressions(
        exp_items,
        "observed_false_positive_rate",
        "bits_per_item",
        "Compression rate vs observed false positive rate",
        project_root / "results/compression_vs_fpr.png",
        "expected_items",
    )

    plot_compressions(
        exp_fpr,
        "n_inserted",
        "memory_bytes",
        "total memory size (Bytes) vs inserted elements",
        project_root / "results/elements_vs_size.png",
        "desired_false_positive_rate",
    )

    plot_compressions(
        exp_items,
        "theoretical_false_positive_rate",
        "observed_false_positive_rate",
        "observed vs theoretical false positive rates",
        project_root / "results/exp_vs_obs_fpr_by_item.png",
        "expected_items",
    )

    plot_compressions(
        exp_fpr,
        "theoretical_false_positive_rate",
        "observed_false_positive_rate",
        "observed vs theoretical false positive rates",
        project_root / "results/exp_vs_obs_fpr_by_fpr.png",
        "desired_false_positive_rate",
    )

    print("Plots saved in results/.")
