# quick_demo.py

from bloom_filter import BloomFilter

if __name__ == "__main__":
    bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)

    words = ["apple", "banana", "cherry", "mango"]

    print("Inserting items...")
    for w in words:
        bf.add(w)

    print("\nChecking inserted items:")
    for w in words:
        print(w, "->", bf.contains(w))

    print("\nChecking non-inserted items:")
    test_words = ["orange", "grape", "pineapple"]
    for w in test_words:
        print(w, "->", bf.contains(w))

    print("\nInfo:")
    print("Bit array size:", bf.m)
    print("Hash functions:", bf.k)
    print("Memory (bytes):", bf.memory_bytes())
    print("Fill ratio:", bf.fill_ratio())
    print("Estimated FPR:", bf.theoretical_false_positive_rate())
