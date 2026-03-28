"""Unit tests for the BloomFilter implementation."""

import random
import string
import unittest

from bloom_filter import BloomFilter

RANDOM_SEED = 42


def random_string(length: int = 12) -> str:
    """Generate a random lowercase alphanumeric string."""
    return "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )


class TestBloomFilter(unittest.TestCase):
    """Test cases for BloomFilter behavior."""

    def test_insert_and_lookup(self) -> None:
        """Ensure inserted items are found in the filter."""
        bloom_filter = BloomFilter(1000, 0.01)
        items = ["apple", "banana", "cherry"]

        for item in items:
            bloom_filter.add(item)

        for item in items:
            self.assertTrue(bloom_filter.contains(item))

    def test_size(self) -> None:
        """Test if the memory size stays constant but count is updated."""
        random.seed(RANDOM_SEED)
        bloom_filter = BloomFilter(1000, 0.01)
        items = [random_string() for _ in range(500)]
        start_size = bloom_filter.memory_bytes()

        self.assertTrue(bloom_filter.count == 0)
        self.assertTrue(bloom_filter.fill_ratio() == 0.0)

        bloom_filter.add(items[0])

        self.assertTrue(bloom_filter.count == 1)
        self.assertTrue(bloom_filter.memory_bytes() == start_size)
        self.assertLess(0.0, bloom_filter.fill_ratio())

        for item in items:
            bloom_filter.add(item)

        self.assertTrue(bloom_filter.count == 500)
        self.assertTrue(bloom_filter.memory_bytes() == start_size)
        self.assertLess(bloom_filter.fill_ratio(), 0.35)

    def test_repeated_inserts(self) -> None:
        """Test if repeated inserts do not influence the internal state."""
        random.seed(RANDOM_SEED)
        bloom_filter = BloomFilter(1000, 0.01)
        items = [random_string() for _ in range(500)]

        for item in items:
            bloom_filter.add(item)

        start_ratio = bloom_filter.fill_ratio()
        start_size = bloom_filter.memory_bytes()
        self.assertTrue(bloom_filter.count == 500)

        for item in items:
            bloom_filter.add(item)
        self.assertTrue(bloom_filter.count == 500)
        self.assertTrue(bloom_filter.fill_ratio() == start_ratio)
        self.assertTrue(bloom_filter.memory_bytes() == start_size)

    def test_no_false_negatives(self) -> None:
        """Ensure inserted items do not produce false negatives."""
        random.seed(RANDOM_SEED)
        bloom_filter = BloomFilter(1000, 0.01)
        items = [random_string() for _ in range(500)]

        for item in items:
            bloom_filter.add(item)

        for item in items:
            self.assertTrue(item in bloom_filter)

    def test_false_positive_rate(self) -> None:
        """Check that the observed false positive rate stays acceptable."""
        random.seed(RANDOM_SEED)
        bloom_filter = BloomFilter(5000, 0.01)

        inserted = {random_string() for _ in range(5000)}
        for item in inserted:
            bloom_filter.add(item)

        trials = 2000
        false_positives = 0

        for _ in range(trials):
            candidate = random_string()
            if candidate not in inserted and candidate in bloom_filter:
                false_positives += 1

        observed = false_positives / trials
        self.assertLess(
            observed, bloom_filter.theoretical_false_positive_rate() * 1.05
        )


if __name__ == "__main__":
    unittest.main()
