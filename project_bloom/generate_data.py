# generate_data.py

import random
import string
from pathlib import Path


def generate_random_strings(n, length=12):
    alphabet = string.ascii_lowercase + string.digits
    return [
        "".join(random.choices(alphabet, k=length))
        for _ in range(n)
    ]


def generate_dna_sequences(n, length=40):
    alphabet = "ACGT"
    return [
        "".join(random.choices(alphabet, k=length))
        for _ in range(n)
    ]


def save_lines(path, data):
    Path(path).write_text("\n".join(data), encoding="utf-8")


if __name__ == "__main__":
    random.seed(42)

    Path("data").mkdir(exist_ok=True)

    random_strings = generate_random_strings(200000)
    dna_sequences = generate_dna_sequences(200000)

    save_lines("data/random_strings.txt", random_strings)
    save_lines("data/dna_sequences.txt", dna_sequences)

    print("Datasets generated.")