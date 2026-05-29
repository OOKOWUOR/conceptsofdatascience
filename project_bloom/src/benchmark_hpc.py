# benchmark.py
"""Benchmarking script for the Bloom filter implementation on hpc."""

import benchmark as bm
import random
from pathlib import Path
from typing import Any, Dict, List

if __name__ == "__main__":
    here = Path(__file__).resolve()
    project_root = here.parent.parent

    random.seed(bm.RANDOM_SEED)

    random_data = bm.load_data(project_root / "data/hpc/random_strings.txt")
    dna_data = bm.load_data(project_root / "data/hpc/dna_sequences.txt")

    rows: List[Dict[str, Any]] = []
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=1000000)
    )
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=1000000))

    bm.save_results(project_root / "results/hpc/benchmark_results.csv", rows)

    rows.clear()
    rows.extend(bm.benchmark_dataset("random", random_data))
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=125000)
    )
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=150000)
    )
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=200000)
    )
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=250000)
    )
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=500000)
    )
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=1000000)
    )
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=2000000)
    )
    rows.extend(bm.benchmark_dataset("dna", dna_data))
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=125000))
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=150000))
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=200000))
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=250000))
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=500000))
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=1000000))
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=2000000))

    bm.save_results(
        project_root / "results/hpc/benchmark_expected_items.csv", rows
    )

    rows.clear()
    rows.extend(
        bm.benchmark_dataset("random", random_data, expected_items=1000000)
    )
    rows.extend(
        bm.benchmark_dataset(
            "random", random_data, expected_items=1000000, fpr=0.05
        )
    )
    rows.extend(
        bm.benchmark_dataset(
            "random", random_data, expected_items=1000000, fpr=0.1
        )
    )
    rows.extend(
        bm.benchmark_dataset(
            "random", random_data, expected_items=1000000, fpr=0.5
        )
    )
    rows.extend(bm.benchmark_dataset("dna", dna_data, expected_items=1000000))
    rows.extend(
        bm.benchmark_dataset("dna", dna_data, expected_items=1000000, fpr=0.05)
    )
    rows.extend(
        bm.benchmark_dataset("dna", dna_data, expected_items=1000000, fpr=0.1)
    )
    rows.extend(
        bm.benchmark_dataset("dna", dna_data, expected_items=1000000, fpr=0.5)
    )

    bm.save_results(
        project_root / "results/hpc/benchmark_expected_fpr.csv", rows
    )
