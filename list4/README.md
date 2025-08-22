# Hashing

## Files

- `list4.py` contains functions that return the hash value for a given bitstring, and a function that suggests the number of bands and rows per band for MinHash signatures based on a given similarity threshold.  

- `test_list4.py` contains unit tests for all functions from `list4.py`.  

- `36.py` generates a set of random bitstrings, computes the minimal SHA1 hash over concatenations, and estimates the maximal feasible input size for the tested configuration.  

- `37.py` builds sets of short words from `text1`, `text2`, and `text3` from `nltk.book`, computes 100-minhash signatures, and estimates Jaccard similarity between the sets.  

- `38.py` computes the exact Jaccard similarity of the sets from `37.py` and compares it with the MinHash estimates.  

- `39.py` creates progressively reduced subsets of S1, applies the banding technique, and experiments with parameters to find similar sets.  
