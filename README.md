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
- test_false_positive_rate: test false positive rate. Here it is tested that our implementation stays under the theoretical false positive rate increased with an error margin of 5%.

### Hashing tests

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
- Insertion time
  - We see that the insertion time quite stable is and linearly increases with insertions for all data types. The data type itself does not seem to matter a lot, but the length of the data type determines the hashing time and thus the insertion time as well.
  - A total insertion time of about 0.3 seconds is recorded when inserting 100.000 elements and increases quite stable. There is a bit of fluctuation at the start (steap increase followed by a slower increase, again a higher increase), but afterwards the increase is quite stable.
  - The average insertion time tells the same story, with highest insertion times at 1000 and 5000 elements, at 10.000 it's at a stable release to increase again for 25.000 and then remain stable for the other elements. <span style="color:red">WHY???</span>
- Search time
  - Absent elements:
    - The lookup time is stable and increases linearly with the amount of added data for all data types. Again, only the sentences show a higher lookup time, because the hash functions need more time to calculate the hashes of bigger strings.
    - The total lookup time is also about 0.3 seconds when looking for 100.000 elements and increases in a nicely linear way. The actual increase depends a bit on the data type, with English sentences having a steeper slope because each lookup takes a bit longer.
    - The average lookup time is a bit hectic at the start, but seems to stabelize when more elements were inserted. Although, we can still see an increasing trend. This is probably because the code looks untill it finds one bit that is not set and this takes longer when more insertions (more bits set to 1 that coincidentally coalide) were done. Because this is also up to chance, it might also explain the hectic behavior at the start.
  - Present elements:
    - This behaves quite similarly as the lookup time, but there are some differences
    - For the total lookup time, it seems to take a bit longer than for the absent elements with about 0.35 seconds for 100.000 elements. Again, this is probably because it needs to check each and every result of the hash functions.
    - Here the average lookup time is quite stable and stays more or less constant even with higher insertion values.
    - <span style="color:red">ARE THE LOOKUP TIMES HECTIC AT START OR ARE THE DIFFERENCES NEGLECTIBLE???</span>
- Storage and compression
  - Total storage stays stable from creation, no matter how many elements are inserted.
  - The amount of bits per item decreases logaritmically with increasing inserted elements.
  - It can be seen that with by decreasing the desired false positive rate (or increasing the amount of expected inserts) the total memory increases right from the build of the bloom filter.
  - It can also be seen that the compression rate (amount of bits for each element) has a logaritmic relation with the false positive rate. With the compression rate decreasing when more false positives are perceived.
- False positive rates
  - It can be seen that the observed false positive rate is quite consistent with the theoretical expectations. They stay quite stable up to 50.000 elements (expected elements 100.000 and false positive rate of 0.01) and then increasing quite steeply to 0.01 at 100.000 elements.
  - The observed false positive rate has almost a one on one relationship with the theoretical false positive rate, but tends to increase a bit faster. This can be best seen for the expected false positive rate of 0.5 where the observed false positive rate reaches 0.5 while the theoretical value is still only at 0.4. <span style="color:red">IS THIS CORRECT OR AN ERROR IN THE CODE???</span> On the other side, if the expected amount of elements to be inserted is varied, the relationship seems to be nicely one on one.
- False negative rates
  - These stay stable at zero.
- <span style="color:red">ADD REFERENCES TO THE IMAGE FILE!!!</span>

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