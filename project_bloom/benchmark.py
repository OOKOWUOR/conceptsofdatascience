# benchmark.py

import time
import random
import csv
from pathlib import Path

from bloom_filter import BloomFilter


def load_data(path):
    return Path(path).read_text(encoding="utf-8").splitlines()


def benchmark_dataset(name, data, expected_items=100000, fpr=0.01):
    bf = BloomFilter(expected_items, fpr)

    steps = [1000, 5000, 10000, 25000, 50000, 100000]
    results = []

    max_n = max(steps)
    data = data[:max_n * 2]

    inserted = data[:max_n]
    negatives = data[max_n:max_n * 2]

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

        results.append({
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
        })

    return results


def save_results(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    random.seed(42)
    Path("results").mkdir(exist_ok=True)

    random_data = load_data("data/random_strings.txt")
    dna_data = load_data("data/dna_sequences.txt")

    rows = []
    rows.extend(benchmark_dataset("random", random_data))
    rows.extend(benchmark_dataset("dna", dna_data))

    save_results("results/benchmark_results.csv", rows)

    print("Benchmark done.")