from collections import Counter 

def bitstring_hamming(b, n):
    '''
    Returns a list of all bitstrings such that the Hamming distance between each bitstring and given bitstring is equal to n

            Parameters:
                    b (str): The given string
                    n (int): The Hamming distance

            Returns:
                    b_pri (list of str): A list of bitstrings b' with Hamming distance n from b
    '''    
    ham_dist = 0
    all_bitstring = ['']
    b_pri = []
    length = len(b)

    if length == 0:
        return ['']
    for i in range(length):
        new_all_bitstrings = []
        for bitstring in all_bitstring:
            new_all_bitstrings.append(bitstring + '0') 
            new_all_bitstrings.append(bitstring + '1')
        all_bitstring = new_all_bitstrings 

    for bitstring in all_bitstring:
        ham_dist = 0
        for elem1, elem2 in zip(b,bitstring):
            if elem1 != elem2:
                ham_dist += 1
        if(ham_dist == n):
            b_pri.append(bitstring)
    return b_pri

def levenshtein(x, y):
    '''
    Returns the Levenshtein distance between two given strings

            Parameters:
                    x (str): The given string
                    y (str): The second given string, which may have a different length from string x.
            Returns:
                   tab[i][j] (int): The Levenshtein distance between two strings x and y
    '''    
    a = len(x) + 1
    b = len(y) + 1
    tab = [0] * a
    for i in range(a):
        tab[i] = [0] * b
    for i in range(a):
            tab[i][0] = i
    for j in range (b):
            tab[0][j] = j

    for i in range(1, a):
       for j in range(1, b):
            if x[i-1]==y[j-1]:
                cost = 0
            else:
                cost = 1
            tab[i][j] = min(tab[i-1][j] + 1,tab[i][j-1] + 1,tab[i-1][j-1] + cost)  
 
    return tab[i][j]

def set_jaccard(x, y):
    '''
    Returns the Jaccard score for two sets x and y

            Parameters:
                    x (set): The given set
                    y (set): The given set

            Returns:
                    result (float): The Jaccard score for two given sets
    '''    
    a = len(x)
    b = len(y)
    if a==b==0:
        raise ValueError('Both sets are empty')   
    same_elements = x.intersection(y)
    unique_elements = x.union(y)
    result = len(same_elements)/len(unique_elements)   
    return result

def  bag_jaccard(x, y):
    '''
    Returns the Jaccard score for two strings x and y represented as bags of words
            Parameters:
                    x (str): The given string
                    y (str): The given string

            Returns:
                    result (float): The Jaccard score for the two given strings represented as bags of words.
    '''    
    a=Counter(x.split())
    b=Counter(y.split())
    same_elements = sum((a & b).values())
    unique_elements = sum((a | b).values())
    if unique_elements == 0:
        raise ValueError('Both sets are empty')
    result = same_elements/unique_elements
    return result

def  shingles(s, k):
    '''
    Returns the set of all k-shingles of the given string and natural number k

            Parameters:
                    s (str): The given string.
                    k (int): The length of the k-shingles

            Returns:
                    shingles (set): The set of all k-shingles of the given string s
    '''    
    shingles=[]
    i = 0
    if k == 0:
        return shingles
    for i, item in enumerate(s):
        count = 0
        elem = ''
        for a in s[i:]:
            if count < k:
                elem += a
                count += 1
        if count == k:  
            if elem not in shingles: 
                shingles.append(elem)
    return shingles


def  diameter(S, d):
    '''
    Calculates the diameter of the metric space (S, d)

            Parameters:
                    S (set): The given a set of words
                    d (function): The distance function

            Returns:
                    max_dist (Int): the diameter of the metric space (S, d)
    '''                       
    max_dist=0
    
    for worda in S:
        for wordb in S:
            dist=d(worda, wordb)
            if (dist > max_dist):
                 max_dist= dist
    return max_dist  
