# bloom_filter.py

from __future__ import annotations

import hashlib
import math


class BloomFilter:
    def __init__(
        self, expected_items: int, false_positive_rate: float
    ) -> None:
        if expected_items <= 0:
            raise ValueError("expected_items must be > 0")
        if not 0 < false_positive_rate < 1:
            raise ValueError("false_positive_rate must be between 0 and 1")

        self.expected_items = expected_items
        self.false_positive_rate = false_positive_rate

        self.m = self._optimal_bit_array_size(
            expected_items, false_positive_rate
        )
        self.k = self._optimal_hash_count(self.m, expected_items)

        self.bit_array = bytearray(math.ceil(self.m / 8))
        self.count = 0

    @staticmethod
    def _optimal_bit_array_size(n: int, p: float) -> int:
        return math.ceil(-(n * math.log(p)) / (math.log(2) ** 2))

    @staticmethod
    def _optimal_hash_count(m: int, n: int) -> int:
        return max(1, round((m / n) * math.log(2)))

    @staticmethod
    def _to_bytes(item: str) -> bytes:
        return item.encode("utf-8")

    def _hashes(self, item: str) -> list[int]:
        data = self._to_bytes(item)

        h1 = int(hashlib.sha256(data).hexdigest(), 16)
        h2 = int(hashlib.md5(data).hexdigest(), 16)
        hashlib.sha256()

        return [((h1 + i * h2) % self.m) for i in range(self.k)]

    def _set_bit(self, index: int) -> None:
        byte_index = index // 8
        bit_index = index % 8
        self.bit_array[byte_index] |= 1 << bit_index

    def _get_bit(self, index: int) -> int:
        byte_index = index // 8
        bit_index = index % 8
        return (self.bit_array[byte_index] >> bit_index) & 1

    def add(self, item: str) -> None:
        for position in self._hashes(item):
            self._set_bit(position)
        self.count += 1

    def __contains__(self, item: str) -> bool:
        return all(self._get_bit(position) for position in self._hashes(item))

    def contains(self, item: str) -> bool:
        return item in self

    def fill_ratio(self) -> float:
        ones = sum(bin(byte).count("1") for byte in self.bit_array)
        return ones / self.m

    def memory_bytes(self) -> int:
        return len(self.bit_array)

    def theoretical_false_positive_rate(self) -> float:
        return (1 - math.exp(-self.k * self.count / self.m)) ** self.k
