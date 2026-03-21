# test_bloom_filter.py

import unittest
import random
import string

from bloom_filter import BloomFilter


def random_string(length: int = 12):
    return "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )


class TestBloomFilter(unittest.TestCase):

    def test_insert_and_lookup(self):
        bf = BloomFilter(1000, 0.01)
        items = ["apple", "banana", "cherry"]

        for item in items:
            bf.add(item)

        for item in items:
            self.assertTrue(bf.contains(item))

    def test_no_false_negatives(self):
        bf = BloomFilter(1000, 0.01)
        items = [random_string() for _ in range(500)]

        for item in items:
            bf.add(item)

        for item in items:
            self.assertTrue(item in bf)

    def test_false_positive_rate(self):
        bf = BloomFilter(5000, 0.01)

        inserted = {random_string() for _ in range(5000)}
        for item in inserted:
            bf.add(item)

        trials = 2000
        false_positives = 0

        for _ in range(trials):
            x = random_string()
            if x not in inserted and x in bf:
                false_positives += 1

        observed = false_positives / trials
        self.assertLess(observed, 0.03)


if __name__ == "__main__":
    unittest.main()
