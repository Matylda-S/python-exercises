from hashlib import sha1
import random
from itertools import combinations

def random_bit_string_generator(n):
    """
    Generates a set of n random bitstrings of length 100

                Parameters:
                        n (int): The number of bitstrings to generate

                Returns:
                        S (set): A set of n random bitstrings.
    """
    S = set()
    for j in range(n):
        bit_string = ''
        for i in range(100):
            bit = random.choice('01')
            bit_string += bit    
        S.add(bit_string)        
    return S


def find_min_sha1(S):
    """
    Finds the minimum SHA-1 hash value for all possible pairs of bitstrings in the set S

                Prameters
                        S (set): A set of bitstrings

                Returns:
                    min_SHA (str): The minimum SHA-1 hash value
    """
    min_SHA='f' * 40
    for string1, string2 in combinations(S, 2):
        SHA_value =sha1((string1 + string2).encode()).hexdigest()
        if  SHA_value < min_SHA:
            min_SHA = SHA_value
    return min_SHA

if __name__ == "__main__":
    n=1000
    result=find_min_sha1(random_bit_string_generator(n))
    print("Minimal sha1(x||y) is equal to: ", result)

    