# Bloom Filter Project (2025–2026)

## 📌 Overview
This project implements a **Bloom filter**, a probabilistic data structure used for efficient membership testing with a controlled false positive rate. The project was worked out by Silas Ooko and Saïd De Wolf.

## Consistency and reproducability
Small and consistent commits were used to have a good log of the evolution of the producion of the project. To contain the development from the main code, all development was done in branches. Finally, a workflow was set up to check if all written tests still pass when a pull request from a branch to the main is made.
The other action to increase consistency and reproducability is that all used conda environments were exported to .yml-files and stored in the repository. In this way they can be used to reproduce the exact environments on other systems.

## Code quality
To make sure the code is up to a certain standard, each pull request from a branch to main needs a review from the other team member. On top of this, the workflow for the pull requests to main also include the mypy and flake8 commands to see if the code is written consistent and holds to general code conventions.

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

## Testing
### Implementation tests
The actual implementation has tests written in project_bloom/tests/test_bloom_filter.py. These tests some of the basic behavior we wish to see in the bloom filter.
- test_insert_and_lookup: tests if every inserted element can also be found. This shows that no inserted elements are lost.
- test_size: tests the memory usage and fill ratio on insertion. This shows that with increasing inserts the fill ratio increases, but the memory usage stays stable.
- test_repeated_inserts: tests memory usage and fill ratio on repeated inserts. This shows that our system is stable and the fill ratio (and memory usage) stays stable if the same set of elements is inserted a second time.
- test_no_false_negatives: tests for false negatives. This shows that the basic behavior of allowing no false negatives is actually met.
- test_false_positive_rate: test false positive rate. Here it is tested that our implementation stays under the theoretical false positive rate increased with an error margin of 5%. For this also a plot was generated for both theoretical as actual false positive rate, so that the behavior of both can be compared.

### Hashing tests
<span style="color:red">
-------------------------------TODO--------------------------------------------
These hash functions should be tested to verify that they produce appropriate values.
Note that these hash functions may work well for certain data (e.g., natural language words) but not so well for other data (e.g., random strings or DNA). Test with at least two data types.
-------------------------------------------------------------------------------
</span>

## 📊 Results & Discussion

### General conclusions
- The insertion time increases approximately linearly with the number of elements.
- Lookup time remains fast and relatively stable, confirming O(k) complexity.
- The observed false positive rate increases as more elements are inserted.
- When the number of elements approaches/exceeds the expected capacity, the false positive rate rises significantly.
- There were no false negatives observed.
- The Bloom filter is highly memory efficient, using only a few bits per element when it reaches the expected capacity. The total amount of memory is fixed at generation and thus already takes up this memory even if nothing has been inserted yet.
- Performance is similar across datasets, but slight differences may occur due to hash distribution. This is especially visible when larger elements (such as sentences instead of words) are being hashed.

### Local benchmarking results
The benchmarking was done for different amount of insertions and bloom filters defined with different parameters (expected insertion amount and expected false positive rates). Each combination was then run 10 times for which the average value was taken. This was done for four different data types: random alpha numeric strings, short DNA sequences, English words and finally English sentences. For the last two the Natural Language Toolkit (NLTK) (Bird et al., 2009) was used with most of the contained databases:
- The contained words set was used for the English words
- gutenberg, brown, reuters, inaugural, webtext and nps_chat were used for the English sentences

The actual benchmarks results are as following:
- Insertion time
  - We see that the insertion time quite stable is and linearly increases with insertions for all data types. The data type itself does not seem to matter a lot, but the length of the data type determines the hashing time and thus the insertion time as well.
  - A total insertion time (total_insert_time.png) of about 0.40 (or 0.50 for the sentences) seconds is recorded when inserting 100.000 elements and increases quite stable. Here the effect of the hashing functions can be seen as the dataset of English sentences has an obvious steeper slope than the other datasets.
  - The average insertion time (avg_insert_time.png) behaves a bit unstable when inserting smaller values, but stabelizes quite nicely when increasing the amount of insertions. A small increase is noticeable, this is because the insert first checks if the element is already present before inserting. This operation takes longer when the bloom filter starts to get filled up because it will need to check all bits of the hash instead of only up to the point where the first false is generated. However, we do see that the random dataset reacts less stable then the others<span style="color:red">WHY???</span>
- Search time
  - Absent elements:
    - The lookup time is stable and increases linearly with the amount of added data for all data types. Again, only the sentences show a higher lookup time, because the hash functions need more time to calculate the hashes of bigger strings.
    - The total lookup time (total_search_absent_time.png) is also about 0.20 to 0.25 seconds when looking for 100.000 elements and increases in a nicely linear way. The actual increase depends a bit on the data type, with English sentences having a steeper slope because each lookup takes a bit longer.
    - The average lookup time (avg_search_absent_time.png) is less stable at the start, but seems to stabelize when more elements were checked. Although, we can still see an increasing trend. This is probably because the code looks untill it finds one bit that is not set and this takes longer when more insertions (more bits set to 1 that coincidentally coalide) were done. Because this is also up to chance, it might also explain the hectic behavior at the start.
  - Present elements:
    - This behaves quite similarly as the absent lookup time, but there are some differences
    - For the total lookup time (total_search_present_time.png), it seems to take a bit longer than for the absent elements with about 0.25 to 0.30 seconds for 100.000 elements.
    - Here the average lookup time (avg_search_present_time.png) is quite stable from 25.000 elements on and stays more or less constant even with higher insertion values. Again, only the random data set shows more variation than the other data sets.
    - <span style="color:red">ARE THE LOOKUP TIMES HECTIC AT START OR ARE THE DIFFERENCES NEGLECTIBLE???</span>
- Storage and compression
  - Total storage stays stable from creation, no matter how many elements are inserted (total_storage.png).
  - The amount of bits per item decreases logaritmically with increasing inserted elements (used_bits_per_item.png).
  - It can be seen that with by decreasing the desired false positive rate (or increasing the amount of expected inserts) the total memory increases right from the build of the bloom filter (elements_vs_size.png).
  - It can also be seen that the compression rate (amount of bits for each element) has a logaritmic relation with the false positive rate. With the compression rate decreasing when more false positives are perceived (compression_vs_fpr.png).
- False positive rates
  - It can be seen that the observed false positive rate is quite consistent with the theoretical expectations. They stay quite stable up to 50.000 elements (expected elements 100.000 and false positive rate of 0.01) and then increasing quite steeply to 0.01 at 100.000 elements (observed_fpr.png, theoretical_fpr.png).
  - The observed false positive rate has almost a one on one relationship with the theoretical false positive rate. This is the case when varying the false positive rate (exp_vs_obs_fpr_by_fpr.png). With only the false positive rate of 0.5 increases a bit faster then the theoretical expected values reaching 0.5 while the theoretical value is still only at 0.4. <span style="color:red">IS THIS CORRECT OR AN ERROR IN THE CODE???</span> On the other side, if the expected amount of elements to be inserted is varied (exp_vs_obs_fpr_by_item.png), the relationship seems to be nicely one on one.
- False negative rates
  - These stay stable at zero (observed_fneg.png).

### HPC benchmarking results
---

## 📁 Project Structure
- .github/workflows: files containing the workflows to run at pull request from branch to main
- project_bloom: the actual project
  - bash: the file to run on HPC
  - conda: stored .yml-files containing the used conda environments
  - data: files containing the generated data for benchmarking
  - docs: <span style="color:red">DO WE USE THIS OR PLACE DOCS AT SOURCE???</span>.
  - results: benchmarking results and generated plots <span style="color:red">DO WE SPLIT THIS UP IN LOCAL/HPC???</span>.
  - src: the actual code for building, using and benchmarking the bloom filter
  - tests: the files containing the tests for the bloom filter
  - setup.py
- README.md