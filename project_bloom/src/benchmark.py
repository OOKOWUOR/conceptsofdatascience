# benchmark.py
"""Benchmarking script for the Bloom filter implementation."""

import csv
import random
import time
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from bloom_filter import BloomFilter

BENCHMARK_STEPS = [1000, 5000, 10000, 25000, 50000, 100000]
RANDOM_SEED = 42


def load_data(path: Path) -> List[str]:
    """Load data from a text file, returning a list of lines."""
    return path.read_text(encoding="utf-8").splitlines()


def _prepare_dataset_slices(
    data: Sequence[str],
) -> Tuple[List[str], List[str]]:
    """Prepare inserted and negative samples for benchmarking."""
    max_n = max(BENCHMARK_STEPS)
    if len(data) < max_n * 2:
        raise ValueError(
            (
                f"data must be at least of size {max_n*2},",
                f" but is of size {len(data)}",
            )
        )
    inserted = list(data[:max_n])
    negatives = list(data[max_n : max_n * 2])
    return inserted, negatives


def _time_insertions(bloom_filter: BloomFilter, items: Sequence[str]) -> float:
    """Measure the time taken to insert items into the Bloom filter."""
    start = time.perf_counter()
    for item in items:
        bloom_filter.add(item)
    return time.perf_counter() - start


def _measure_searches(
    bloom_filter: BloomFilter, items: Sequence[str]
) -> Dict[str, float]:
    """Measure search time and number of positive matches."""
    positives = 0

    start = time.perf_counter()
    for item in items:
        if bloom_filter.contains(item):
            positives += 1
    elapsed = time.perf_counter() - start

    return {
        "search_time_sec": elapsed,
        "positives": positives,
    }


def _collect_filter_metrics(
    bloom_filter: BloomFilter, inserted_count: int
) -> Dict[str, float]:
    """Collect Bloom filter metrics for a benchmark step."""
    return {
        "theoretical_false_positive_rate": (
            bloom_filter.theoretical_false_positive_rate()
        ),
        "memory_bytes": bloom_filter.memory_bytes(),
        "fill_ratio": bloom_filter.fill_ratio(),
        "bits_per_item": bloom_filter.m / inserted_count,
    }


def _build_result_row(
    name: str,
    inserted_count: int,
    timing_metrics: Dict[str, float],
    present_metrics: Dict[str, float],
    absent_metrics: Dict[str, float],
    filter_metrics: Dict[str, float],
    expected_items: int,
    desired_false_positive_rate: float,
) -> Dict[str, Any]:
    """Build a single benchmark result row."""
    return {
        "dataset": name,
        "n_inserted": inserted_count,
        "insert_time_sec": timing_metrics["insert_time_sec"],
        "present_search_time_sec": present_metrics["search_time_sec"],
        "absent_search_time_sec": absent_metrics["search_time_sec"],
        "false_negatives": inserted_count - int(present_metrics["positives"]),
        "observed_false_positive_rate": (
            absent_metrics["positives"] / inserted_count
        ),
        "theoretical_false_positive_rate": filter_metrics[
            "theoretical_false_positive_rate"
        ],
        "memory_bytes": filter_metrics["memory_bytes"],
        "fill_ratio": filter_metrics["fill_ratio"],
        "bits_per_item": filter_metrics["bits_per_item"],
        "expected_items": expected_items,
        "desired_false_positive_rate": desired_false_positive_rate,
    }


""" def _benchmark_step(
    bloom_filter: BloomFilter,
    name: str,
    dataset_parts: Dict[str, Any],
    step: int,
) -> Tuple[Dict[str, Any], int]:
    "Run one benchmark step and return the result row and
    the new insertion index."
    inserted = dataset_parts["inserted"]
    negatives = dataset_parts["negatives"]
    inserted_so_far = dataset_parts["inserted_so_far"]

    new_items = inserted[inserted_so_far:step]
    present_items = inserted[:step]

    timing_metrics = {
        "insert_time_sec": _time_insertions(bloom_filter, new_items),
    }
    present_metrics = _measure_searches(bloom_filter, present_items)
    absent_metrics = _measure_searches(bloom_filter, negatives[:step])
    filter_metrics = _collect_filter_metrics(bloom_filter, step)

    dataset_parts["inserted_so_far"] = step

    result_row = _build_result_row(
        name,
        step,
        timing_metrics,
        present_metrics,
        absent_metrics,
        filter_metrics,
        bloom_filter.expected_items,
        bloom_filter.false_positive_rate,
    )
    return result_row, step """


def _benchmark_step(
    expected_items: int,
    fpr: float,
    name: str,
    dataset_parts: Dict[str, Any],
    step: int,
) -> Tuple[Dict[str, Any], int]:
    """Run one benchmark step and return the result row and
    the new insertion index."""
    bloom_filter = BloomFilter(expected_items, fpr)

    inserted = dataset_parts["inserted"]
    negatives = dataset_parts["negatives"]

    present_items = inserted[:step]

    timing_metrics = {
        "insert_time_sec": _time_insertions(bloom_filter, present_items),
    }
    present_metrics = _measure_searches(bloom_filter, present_items)
    absent_metrics = _measure_searches(bloom_filter, negatives[:step])
    filter_metrics = _collect_filter_metrics(bloom_filter, step)

    dataset_parts["inserted_so_far"] = step

    result_row = _build_result_row(
        name,
        step,
        timing_metrics,
        present_metrics,
        absent_metrics,
        filter_metrics,
        bloom_filter.expected_items,
        bloom_filter.false_positive_rate,
    )
    return result_row, step


def benchmark_dataset(
    name: str, data: List[str], expected_items: int = 100000, fpr: float = 0.01
) -> List[Dict[str, Any]]:
    """Benchmark Bloom filter performance on a dataset."""
    # bloom_filter = BloomFilter(expected_items, fpr)
    results: List[Dict[str, Any]] = []
    inserted, negatives = _prepare_dataset_slices(data)
    dataset_parts: Dict[str, Any] = {
        "inserted": inserted,
        "negatives": negatives,
        "inserted_so_far": 0,
    }

    for step in BENCHMARK_STEPS:
        """result_row, _ = _benchmark_step(
            bloom_filter=bloom_filter,
            name=name,
            dataset_parts=dataset_parts,
            step=step,
        )"""
        for _ in range(10):
            result_row, _ = _benchmark_step(
                expected_items=expected_items,
                fpr=fpr,
                name=name,
                dataset_parts=dataset_parts,
                step=step,
            )
            results.append(result_row)

    return results


def save_results(path: Path, values: List[Dict[str, Any]]) -> None:
    """Save benchmark results to a CSV file."""
    with path.open("w", newline="", encoding="utf-8") as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=values[0].keys())
        writer.writeheader()
        writer.writerows(values)


if __name__ == "__main__":
    here = Path(__file__).resolve()
    project_root = here.parent.parent

    random.seed(RANDOM_SEED)

    random_data = load_data(project_root / "data/random_strings.txt")
    dna_data = load_data(project_root / "data/dna_sequences.txt")
    words = load_data(project_root / "data/english_words.txt")
    sentences = load_data(project_root / "data/english_sentences.txt")

    rows: List[Dict[str, Any]] = []
    rows.extend(benchmark_dataset("random", random_data))
    rows.extend(benchmark_dataset("dna", dna_data))
    rows.extend(benchmark_dataset("English words", words))
    rows.extend(benchmark_dataset("English sentences", sentences))

    save_results(project_root / "results/benchmark_results.csv", rows)

    rows.clear()
    rows.extend(benchmark_dataset("random", random_data))
    rows.extend(
        benchmark_dataset("random", random_data, expected_items=125000)
    )
    rows.extend(
        benchmark_dataset("random", random_data, expected_items=150000)
    )
    rows.extend(
        benchmark_dataset("random", random_data, expected_items=200000)
    )
    rows.extend(benchmark_dataset("dna", dna_data))
    rows.extend(benchmark_dataset("dna", dna_data, expected_items=125000))
    rows.extend(benchmark_dataset("dna", dna_data, expected_items=150000))
    rows.extend(benchmark_dataset("dna", dna_data, expected_items=200000))
    rows.extend(benchmark_dataset("English words", words))
    rows.extend(
        benchmark_dataset("English words", words, expected_items=125000)
    )
    rows.extend(
        benchmark_dataset("English words", words, expected_items=150000)
    )
    rows.extend(
        benchmark_dataset("English words", words, expected_items=200000)
    )
    rows.extend(benchmark_dataset("English sentences", sentences))
    rows.extend(
        benchmark_dataset(
            "English sentences", sentences, expected_items=125000
        )
    )
    rows.extend(
        benchmark_dataset(
            "English sentences", sentences, expected_items=150000
        )
    )
    rows.extend(
        benchmark_dataset(
            "English sentences", sentences, expected_items=200000
        )
    )

    save_results(project_root / "results/benchmark_expected_items.csv", rows)

    rows.clear()
    rows.extend(benchmark_dataset("random", random_data))
    rows.extend(benchmark_dataset("random", random_data, fpr=0.05))
    rows.extend(benchmark_dataset("random", random_data, fpr=0.1))
    rows.extend(benchmark_dataset("random", random_data, fpr=0.5))
    rows.extend(benchmark_dataset("dna", dna_data))
    rows.extend(benchmark_dataset("dna", dna_data, fpr=0.05))
    rows.extend(benchmark_dataset("dna", dna_data, fpr=0.1))
    rows.extend(benchmark_dataset("dna", dna_data, fpr=0.5))
    rows.extend(benchmark_dataset("English words", words))
    rows.extend(benchmark_dataset("English words", words, fpr=0.05))
    rows.extend(benchmark_dataset("English words", words, fpr=0.1))
    rows.extend(benchmark_dataset("English words", words, fpr=0.5))
    rows.extend(benchmark_dataset("English sentences", sentences))
    rows.extend(benchmark_dataset("English sentences", sentences, fpr=0.05))
    rows.extend(benchmark_dataset("English sentences", sentences, fpr=0.1))
    rows.extend(benchmark_dataset("English sentences", sentences, fpr=0.5))

    save_results(project_root / "results/benchmark_expected_fpr.csv", rows)

    print("Benchmark done.")
