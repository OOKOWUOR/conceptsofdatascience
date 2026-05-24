# generate_data.py
"""Utility script to generate datasets for benchmarking
the Bloom filter implementation."""
import random
import string
import nltk
from pathlib import Path
from typing import List, Optional
from enum import Enum
from nltk import tokenize as tz


nltk.download("punkt_tab")
nltk.download("gutenberg")
nltk.download("brown")
nltk.download("reuters")
nltk.download("inaugural")
nltk.download("webtext")
nltk.download("nps_chat")


class DataType(Enum):
    """Enumerator with the possible string types."""

    ALFANUM = "alphanumeric"
    DNA = "dna_strings"
    WORD = "english_words"
    SENTENCE = "english_sentences"


def generate_random_strings(
    n: int, data_type: DataType, length: Optional[int] = None
) -> List[str]:
    """Generate a list of random alphanumeric strings."""
    if data_type in (DataType.ALFANUM, DataType.DNA):
        if data_type == DataType.ALFANUM:
            alphabet = string.ascii_lowercase + string.digits
            if length is None:
                length = 12
        else:
            alphabet = "ACGT"
            if length is None:
                length = 40
        return ["".join(random.choices(alphabet, k=length)) for _ in range(n)]
    else:
        if data_type == DataType.WORD:
            options = set(nltk.corpus.words.words())
        else:
            options = tz.sent_tokenize(nltk.corpus.gutenberg.raw())
            options.extend(tz.sent_tokenize(nltk.corpus.brown.raw()))
            options.extend(tz.sent_tokenize(nltk.corpus.reuters.raw()))
            options.extend(tz.sent_tokenize(nltk.corpus.inaugural.raw()))
            options.extend(tz.sent_tokenize(nltk.corpus.webtext.raw()))
            options.extend(tz.sent_tokenize(nltk.corpus.nps_chat.raw()))
            options = set(
                [
                    sentence.replace("\n", " ").replace("\r", " ")
                    for sentence in options
                ]
            )
        return random.sample(population=sorted(options), k=n)


def save_lines(path: Path, data: List[str]) -> None:
    """Save a list of strings to a file, one per line."""
    path.write_text("\n".join(data), encoding="utf-8")


if __name__ == "__main__":
    HERE = Path(__file__).resolve()
    PROJECT_ROOT = HERE.parent.parent

    random.seed(42)

    Path("data").mkdir(exist_ok=True)

    random_strings = generate_random_strings(200000, DataType.ALFANUM)
    dna_sequences = generate_random_strings(200000, DataType.DNA)
    words = generate_random_strings(200000, DataType.WORD)
    sentences = generate_random_strings(200000, DataType.SENTENCE)

    print(random_strings[1:5])
    print(dna_sequences[1:5])
    print(words[1:5])
    print(sentences[10:15])

    save_lines(PROJECT_ROOT / "data/random_strings.txt", random_strings)
    save_lines(PROJECT_ROOT / "data/dna_sequences.txt", dna_sequences)
    save_lines(PROJECT_ROOT / "data/english_words.txt", words)
    save_lines(PROJECT_ROOT / "data/english_sentences.txt", sentences)

    print("Datasets generated.")
