def gen_hash(s, m):
    """
    Computes a hash value for a given bitstring s and parameter m.   
    The function transforms the value from {0, 1}^* into an integer hash value in the range {0, 1, ..., m-1}

            Parameters:
                    s (str): The given bitstring
                    m (int): The given parameter to define the range of hash values
    
            Returns:
                    hash (int): The hash value in the range {0, 1, ..., m-1}
    """
    if m <= 0:
        raise ValueError("Parameter m must greater than zero")
    if not all(elem in '01' for elem in s):
        raise ValueError("Parameter s must be a bitstring")
    a=11
    b=5
    hash=((int(s,2))*a+b)%m
    return hash

def minhash_bands(n, s):
    """
    Suggests number of bands and number of rows in a band based on the number of minhashes and the similarity parameter


            Parameters:
                    n (int): Number of minhashes
                    s (float): Similarity parameter 

            Returns:
                    tuple: A tuple containing the number of bands and the number of rows in band
    """
    if n <= 0:
        raise ValueError("Number of minhashes must be posiitive")
    if not (0 < s < 1):
        raise ValueError("Similarity parameter s must be between 0 and 1")
    num_of_bands = n
    similarity=0
    minimal=100  
    for i in range(1,n+1):
        num_of_bands =i
        num_of_rows = n // num_of_bands
        similarity = (1/float(num_of_bands))**(1/ float(num_of_rows))
        a=abs(similarity - s)
        if minimal>a:
            minimal=a
            best_num_of_bands=num_of_bands
            best_num_of_rows=num_of_rows 
    return (best_num_of_bands,best_num_of_rows)   