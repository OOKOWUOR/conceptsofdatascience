# benchmark.py

import time
import random
import csv
from pathlib import Path
from typing import List, Dict, Any

from bloom_filter import BloomFilter


def load_data(path: Path) -> List[str]:
    return path.read_text(encoding="utf-8").splitlines()


def benchmark_dataset(
    name: str, data: List[str], expected_items: int = 100000, fpr: float = 0.01
) -> List[Dict[str, Any]]:
    bf = BloomFilter(expected_items, fpr)

    steps = [1000, 5000, 10000, 25000, 50000, 100000]
    results: List[Dict[str, Any]] = []

    max_n = max(steps)
    data = data[: max_n * 2]

    inserted = data[:max_n]
    negatives = data[max_n : max_n * 2]

    inserted_so_far = 0

    for n in steps:
        to_insert = inserted[inserted_so_far:n]

        start = time.perf_counter()
        for item in to_insert:
            bf.add(item)
        insert_time = time.perf_counter() - start

        inserted_so_far = n

        start = time.perf_counter()
        for item in inserted[:n]:
            _ = bf.contains(item)
        search_present_time = time.perf_counter() - start

        false_positives = 0
        start = time.perf_counter()
        for item in negatives:
            if bf.contains(item):
                false_positives += 1
        search_absent_time = time.perf_counter() - start

        observed_fpr = false_positives / len(negatives)
        theoretical_fpr = bf.theoretical_false_positive_rate()

        results.append(
            {
                "dataset": name,
                "n_inserted": n,
                "insert_time_sec": insert_time,
                "present_search_time_sec": search_present_time,
                "absent_search_time_sec": search_absent_time,
                "observed_false_positive_rate": observed_fpr,
                "theoretical_false_positive_rate": theoretical_fpr,
                "memory_bytes": bf.memory_bytes(),
                "fill_ratio": bf.fill_ratio(),
                "bits_per_item": bf.m / n,
            }
        )

    return results


def save_results(path: Path, rows: List[Dict[str, Any]]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    HERE = Path(__file__).resolve()
    PROJECT_ROOT = HERE.parent.parent

    random.seed(42)

    random_data = load_data(PROJECT_ROOT / "data/random_strings.txt")
    dna_data = load_data(PROJECT_ROOT / "data/dna_sequences.txt")

    rows: List[Dict[str, Any]] = []
    rows.extend(benchmark_dataset("random", random_data))
    rows.extend(benchmark_dataset("dna", dna_data))

    save_results(PROJECT_ROOT / "results/benchmark_results.csv", rows)

    print("Benchmark done.")
