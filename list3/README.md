# Similarity of Texts
This folder contains solutions to exercises focused on measuring text similarity, including the use of the NLTK library.

## Files
list3.py contains functions that calculate Hamming distance, Levenshtein distance, Jaccard similarity (both for sets and for bags of words), extract k-shingles from a string, and compute the diameter of a metric space based on a given distance function.

test_list3.py contains unit tests for all functions from list3.py.

29.py calculates the diameter of a metric space formed by words from text1 in the nltk.book module, using the restricted Hamming distance.

30.py creates a dictionary mapping each pair of consecutive words in text1 to their Jaccard similarity.

31.py computes the Jaccard similarity between all pairs of texts (text1 to text9) from the nltk.book module.

32.py finds all words in text1 that have a Levenshtein distance of less than 4 from the word “dog”

33.py defines relative edit distance and finds the minimum relative distance between two words in text8 from the nltk.book module.


