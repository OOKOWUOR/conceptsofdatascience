# Bloom Filter Project (2025–2026)


## Proposed README layout (We can clean it)
## Overview

This project outlines the design, implementation, and testing of a Bloom filter, a probabilistic data structure that is used to test data set membership. A Bloom filter, in contrast to more traditional data structures like hash tables or balanced trees, has much faster membership queries, and requires much less memory. This efficiency is achieved by sacrificing a low chance of false positives, even though false negatives are in theory impossible.
This project aimed to implement a fully operational Bloom filter in Python, test its functionality, and understand its performance properties and how its behaviour varies with workloads and input data types. Alongside confirming the theoretical properties of Bloom filters, the project examines more practical considerations in the form of insertion speed, the look-up performance, false positives, storage requirements and compression efficiency. It was implemented on several datasets, consisting of English sentences, English words, DNA sequences, and randomly generated strings, giving a general understanding of the behaviour of Bloom filters with various data types.

## Implementation
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
