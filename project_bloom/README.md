# Bloom Filter Project (2025–2026)

## 📌 Overview
This project implements a **Bloom filter**, a probabilistic data structure used for efficient membership testing with a controlled false positive rate.

---

## 🧠 Features
- Python implementation (modular)
- Multiple hash functions (double hashing)
- No false negatives guarantee
- Controlled false positive rate
- Performance benchmarking
- HPC-ready execution
- Analysis of:
  - False positive rate
  - Time performance
  - Compression efficiency

## 📊 Results & Discussion

- The insertion time increases approximately linearly with the number of elements.
- Lookup time remains fast and relatively stable, confirming O(k) complexity.
- The observed false positive rate increases as more elements are inserted.
- When the number of elements approaches/exceeds the expected capacity, the false positive rate rises significantly.
- The Bloom filter is highly memory efficient, using only a few bits per element.
- Performance is similar across datasets, but slight differences may occur due to hash distribution.
---

## 📁 Project Structure