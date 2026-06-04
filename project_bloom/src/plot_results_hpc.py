# plot_results.py
"""Utility script to generate plots from benchmark results on hpc."""

import pandas as pd
import plot_results as pl
from pathlib import Path

if __name__ == "__main__":
    here = Path(__file__).resolve()
    project_root = here.parent.parent

    data = (
        pd.read_csv(project_root / "results/hpc/benchmark_results.csv")
        .groupby(["dataset", "n_inserted"])
        .agg("mean")
        .reset_index()
    )
    exp_items = (
        pd.read_csv(project_root / "results/hpc/benchmark_expected_items.csv")
        .groupby(["dataset", "n_inserted", "expected_items"])
        .agg("mean")
        .reset_index()
    )
    exp_fpr = (
        pd.read_csv(project_root / "results/hpc/benchmark_expected_fpr.csv")
        .groupby(["dataset", "n_inserted", "desired_false_positive_rate"])
        .agg("mean")
        .reset_index()
    )

    pl.make_plot(
        data,
        "n_inserted",
        "insert_time_sec",
        "Total insertion time (sec) vs inserted items",
        project_root / "results/hpc/total_insert_time.png",
    )

    pl.plot_averages(
        data,
        "n_inserted",
        "insert_time_sec",
        "Average insertion time (sec) vs inserted items",
        project_root / "results/hpc/avg_insert_time.png",
    )

    pl.make_plot(
        data,
        "n_inserted",
        "present_search_time_sec",
        "Total lookup time (present) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/hpc/total_search_present_time.png",
    )

    pl.plot_averages(
        data,
        "n_inserted",
        "present_search_time_sec",
        "Average lookup time (present) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/hpc/avg_search_present_time.png",
    )

    pl.make_plot(
        data,
        "n_inserted",
        "absent_search_time_sec",
        "Total lookup time (absent) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/hpc/total_search_absent_time.png",
    )

    pl.plot_averages(
        data,
        "n_inserted",
        "absent_search_time_sec",
        "Average lookup time (absent) (sec) vs searched items\n"
        + "(# searched items = # inserted items)",
        project_root / "results/hpc/avg_search_absent_time.png",
    )

    pl.make_plot(
        data,
        "n_inserted",
        "false_negatives",
        "Observed false negatives vs inserted items",
        project_root / "results/hpc/observed_fneg.png",
    )

    pl.make_plot(
        data,
        "n_inserted",
        "observed_false_positive_rate",
        "Observed false positive rate vs inserted items",
        project_root / "results/hpc/observed_fpr.png",
    )

    pl.make_plot(
        data,
        "n_inserted",
        "theoretical_false_positive_rate",
        "Theoretical false positive rate vs inserted items",
        project_root / "results/hpc/theoretical_fpr.png",
    )

    pl.make_plot(
        data,
        "n_inserted",
        "bits_per_item",
        "Compression rate: average used bits per item vs inserted items",
        project_root / "results/hpc/used_bits_per_item.png",
    )

    pl.plot_totals(
        data,
        "n_inserted",
        "bits_per_item",
        "Total storage in bits vs inserted items",
        project_root / "results/hpc/total_storage.png",
    )

    pl.plot_compressions(
        exp_items,
        "observed_false_positive_rate",
        "bits_per_item",
        "Compression rate vs observed false positive rate",
        project_root / "results/hpc/compression_vs_fpr.png",
        "expected_items",
    )

    pl.plot_compressions(
        exp_fpr,
        "n_inserted",
        "memory_bytes",
        "total memory size (Bytes) vs inserted elements",
        project_root / "results/hpc/elements_vs_size.png",
        "desired_false_positive_rate",
    )

    pl.plot_compressions(
        exp_items,
        "theoretical_false_positive_rate",
        "observed_false_positive_rate",
        "observed vs theoretical false positive rates",
        project_root / "results/hpc/exp_vs_obs_fpr_by_item.png",
        "expected_items",
    )

    pl.plot_compressions(
        exp_fpr,
        "theoretical_false_positive_rate",
        "observed_false_positive_rate",
        "observed vs theoretical false positive rates",
        project_root / "results/hpc/exp_vs_obs_fpr_by_fpr.png",
        "desired_false_positive_rate",
    )
