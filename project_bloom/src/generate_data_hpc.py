# generate_data_hpc.py
"""Utility script to generate datasets for benchmarking
the Bloom filter implementation on hpc."""

import generate_data as gd
import random
from pathlib import Path

if __name__ == "__main__":
    HERE = Path(__file__).resolve()
    PROJECT_ROOT = HERE.parent.parent

    random.seed(gd.RANDOM_SEED)

    Path("conceptOfDataScience/data/hpc").mkdir(exist_ok=True)

    random_strings = gd.generate_random_strings(
        2000000, gd.DataType.ALFANUM, 60
    )
    dna_sequences = gd.generate_random_strings(2000000, gd.DataType.DNA, 60)

    gd.save_lines(PROJECT_ROOT / "data/hpc/random_strings.txt", random_strings)
    gd.save_lines(PROJECT_ROOT / "data/hpc/dna_sequences.txt", dna_sequences)
