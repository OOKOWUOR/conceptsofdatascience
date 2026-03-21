# generate_data.py

import random
import string
from pathlib import Path
from typing import List


def generate_random_strings(n: int, length: int=12) -> List[str]:
    alphabet = string.ascii_lowercase + string.digits
    return [
        "".join(random.choices(alphabet, k=length))
        for _ in range(n)
    ]


def generate_dna_sequences(n: int, length: int=40) -> List[str]:
    alphabet = "ACGT"
    return [
        "".join(random.choices(alphabet, k=length))
        for _ in range(n)
    ]


def save_lines(path: Path, data: List[str]) -> None:
    path.write_text("\n".join(data), encoding="utf-8")


if __name__ == "__main__":
    HERE = Path(__file__).resolve()
    PROJECT_ROOT = HERE.parent.parent

    random.seed(42)

    Path("data").mkdir(exist_ok=True)

    random_strings = generate_random_strings(200000)
    dna_sequences = generate_dna_sequences(200000)

    save_lines(PROJECT_ROOT / "data/random_strings.txt", random_strings)
    save_lines(PROJECT_ROOT / "data/dna_sequences.txt", dna_sequences)

    print("Datasets generated.")