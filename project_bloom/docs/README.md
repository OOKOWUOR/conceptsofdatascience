# Bloom Filter Project (2025–2026)


## Proposed README layout (We can clean it)
## Overview

This project outlines the design, implementation, and testing of a Bloom filter, a probabilistic data structure that is used to test data set membership. A Bloom filter, in contrast to more traditional data structures like hash tables or balanced trees, has much faster membership queries, and requires much less memory. This efficiency is achieved by sacrificing a low chance of false positives, even though false negatives are in theory impossible.
This project aimed to implement a fully operational Bloom filter in Python, test its functionality, and understand its performance properties and how its behaviour varies with workloads and input data types. Alongside confirming the theoretical properties of Bloom filters, the project examines more practical considerations in the form of insertion speed, the look-up performance, false positives, storage requirements and compression efficiency. It was implemented on several datasets, consisting of English sentences, English words, DNA sequences, and randomly generated strings, giving a general understanding of the behaviour of Bloom filters with various data types.

## Implementation

Bloom filter was developed as a Python library that is easy to read, maintain, and reproduce. It is implemented in the classical Bloom filter architecture where the fixed-size bit array is used and several hash functions are used. In insertion, an element is hashed by multiple independent hash functions and the relevant bit positions in the bit array are marked as one. Membership queries are executed by computing the same hash functions and checking the existence of all the bits. When any of the bits needed are not set, the element is ensured not to be present in the filter. In case all bits are on, the element is reported as potentially present.
The focus was made to make sure that the implementation is modular and extendible. The code was designed to enable various filter sizes, false positives, and data types to be tested without having to change the underlying algorithm. Implementation also involves benchmarking and evaluation tools that are used to produce experimental results as indicated in this report.
The quality of hash functions used in Bloom filters is a key factor in their performance since bad hash distributions can result in a higher rate of collisions and reduced accuracy. Experiments were conducted on several classes of data with highly structured natural language text to entirely random strings to assess the strength of the implementation. This enabled the project to evaluate the ability of the selected hashing strategy to exhibit the same distribution characteristics under a wide workload.

## Correctness Testing
## Experimental Results and Analysis
### Correctness Verification

![Observed False Negatives](../results/observed_fneg.png)

### False Positive Behaviour

![Observed False Positive Rate](../results/observed_fpr.png)
![Theoretical False Positive Rate](../results/theoretical_fpr.png)

![Observed vs Theoretical False Positive Rates](../results/exp_vs_obs_fpr_by_item.png)
![Observed vs Theoretical False Positive Rates by Target Rate](../results/exp_vs_obs_fpr_by_fpr.png)

### Insertion Performance

![Total Insertion Time](../results/total_insert_time.png)
![Average Insertion Time](../results/avg_insert_time.png)

### Lookup Performance

![Total Lookup Time for Absent Elements](../results/total_search_absent_time.png)
![Total Lookup Time for Present Elements](../results/total_search_present_time.png)

![Average Lookup Time for Absent Elements](../results/avg_search_absent_time.png)
![Average Lookup Time for Present Elements](../results/avg_search_present_time.png)

### Memory Usage and Compression Efficiency

![Total Storage in Bits](../results/total_storage.png)
![Average Bits per Item](../results/used_bits_per_item.png)
![Compression Rate versus False Positive Rate](../results/compression_vs_fpr.png)
![Memory Size versus Inserted Elements](../results/elements_vs_size.png)

## Discussion
## Conclusion
## References
- Bird, S., Klein, E., & Loper, E. (2009). Natural language processing with python. O'Reilly Media.
