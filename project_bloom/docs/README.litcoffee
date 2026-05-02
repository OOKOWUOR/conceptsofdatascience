# Bloom Filter Project (2025–2026)

## Overview
Overview
This project outlines the design, implementation and evaluation of a Bloom filter, a probabilistic data structure that is used to effectively test whether an element is in a set. A Bloom filter, in contrast to conventional data structures, is very space-efficient and can be queried very quickly, but at the price of potentially returning a small probability of a false positive.
The purpose of the project was to create a fully working Bloom filter in Python, test its correctness, investigate the performance of it, and learn about its behavioral variations under various circumstances. The work is written according to the project requirements given in the course description but here we are going to explain what was constructed and what was learnt.

## Implementation
The Bloom filter was built as a Python module in a manner that allows it to be easily reproducible in scripts and python codebooks. The code is written in a well-organized format and is simple to read and scale, which makes the design clear and structured.
Fundamentally, it is implemented with the help of a bit array and a family of hash functions. On inserting an element, the element is subjected to several hash functions and the respective positions in the bit array are marked. Membership verification is done by applying the same hash functions and checking by the filter whether all the bits are set.
Special consideration was placed on the clarity of code and documentation, so that every aspect of the implementation is readable and maintainable.
Hash Functions and Data Behavior.
Another key aspect of the project was to design and test the hash functions that the Bloom filter uses. Quality of these functions directly influences the performance, so they were tested on unrelated data, such as natural language words and random generated strings.
The experiments revealed that hash functions can have varying behavior with regards to the structure of the input data. Whereas they did well on structured text, their distribution was less homogenous on random or synthetic data.

## Correctness Testing
In order to make sure that the Bloom filter functions as intended, it was well tested. The filter recognized all elements inserted correctly, which proves the correctness of the implementation. Moreover, we conducted tests on the elements that were not inserted, which enabled us to see how false positives should behave.
These tests indicate that the Bloom filter is practical by preserving its theoretical guarantees.
Performance Evaluation
Large datasets were used to assess the performance of the Bloom filter. The measurements of both insertion and lookup operations were done and as the number of elements was incrementally increased.
The findings indicate that the time taken by the two processes increases in an efficient and predictable way. The time to look up is extremely fast even in the case of large datasets, which underscores one of the most important benefits of Bloom filters.

## False Positive Analysis
One important property of Bloom filters is that they can give false positives. This project investigated the variation in false positive rate with the addition of more elements in the filter.
The experiments confirm that the false positive rate is higher and the more populated the filter the better. With even a larger number of elements that are inserted than the intended capacity, the accuracy is reduced more quickly.

## Space and Compression.
The other notable feature of the Bloom filter is its space efficiency. The Bloom filter consumes a lot less memory as compared to storing full datasets.
The project investigated the dependence of the compression rate on the filter size and the acceptable false positive rate. The findings bring out the trade-off between memory consumption and accuracy: the lower the false positive rate the more space is needed.
Benchmarking
Benchmarking experiments were done on a high-performance computing infrastructure in order to measure performance in a realistic environment. These experiments entailed running the implementation with large data sets and time execution data.
The benchmark performance ensures that the Bloom filter scales effectively and is effective even with heavy workloads.

## Conclusion
This project shows how Bloom filters can be used to offer an efficient solution to speedy and memory efficient membership testing. They are not guaranteed to be accurate, but since they are highly useful because of their low memory requirements and performance in most applicable scenarios.
This project, by implementation and experimentation, demonstrates the tradeoffs of using probabilistic data structures, especially the tradeoff between accuracy, speed, and memory consumption.
