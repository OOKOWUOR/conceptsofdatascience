# generate_data.py
"""Utility script to generate datasets for benchmarking
the Bloom filter implementation."""
import random
import string
from pathlib import Path
from typing import List, Optional
from enum import Enum


class Data_type(Enum):
    ALFANUM = "alphanumeric"
    DNA = "dna_strings"


def generate_random_strings(
    n: int, type: Data_type, length: Optional[int] = None
) -> List[str]:
    """Generate a list of random alphanumeric strings."""
    if type == Data_type.ALFANUM:
        alphabet = string.ascii_lowercase + string.digits
        if length is None:
            length = 12
    elif type == Data_type.DNA:
        alphabet = "ACGT"
        if length is None:
            length = 40
    return ["".join(random.choices(alphabet, k=length)) for _ in range(n)]


def save_lines(path: Path, data: List[str]) -> None:
    """Save a list of strings to a file, one per line."""
    path.write_text("\n".join(data), encoding="utf-8")


if __name__ == "__main__":
    HERE = Path(__file__).resolve()
    PROJECT_ROOT = HERE.parent.parent

    random.seed(42)

    Path("data").mkdir(exist_ok=True)

    random_strings = generate_random_strings(200000, Data_type.ALFANUM)
    dna_sequences = generate_random_strings(200000, Data_type.DNA)

    save_lines(PROJECT_ROOT / "data/random_strings.txt", random_strings)
    save_lines(PROJECT_ROOT / "data/dna_sequences.txt", dna_sequences)

    print("Datasets generated.")
