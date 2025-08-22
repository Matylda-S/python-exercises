from nltk.book import text1
from list3 import set_jaccard
from datasketch import MinHash
from datasketch import MinHashLSH
import random
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import hashlib
def remove_all_punctuation(text):
    text_without_punctuation=[]
    for item in text:
        if item.isalnum():
            text_without_punctuation.append(item)
    return text_without_punctuation 

def reduces_inflected_words(text):
    stems=PorterStemmer()
    text_with_stems=[]
    for item in text:
        text_with_stems.append(stems.stem(item))
    return text_with_stems

def remove_all_stop_words(text):
    words_stop=stopwords.words('english')
    text_without_stopwords=[]
    for item in text:
        item=item.lower()
        if item not in words_stop:
            text_without_stopwords.append(item)
    return text_without_stopwords



def generate_sets(S1):
    """
    Construct sets S1,S2,...,S99 by randomly selecting and removing from S1 1%, 2%,...,99% of elements

            Parameters:
                    S1 (set): The input set from which elements are to be removed.

            Returns:
                    sets (list): A list of sets, where each set is a subset of S1 with an increasing number of elements removed.
    """
    sets=[]
    for i in range(1,100):
        number_of_word_to_remove = int(len(S1) * i/100)
        Si = S1 - set(random.sample(list(S1), number_of_word_to_remove))
        sets.append(Si)
    return sets 

def minhash_sign(S,number_of_minhashes):
    minhash = MinHash(number_of_minhashes)
    for item in S:
        item=item.encode('utf8')
        minhash.update(item)
    return minhash

if __name__ == "__main__":
    texta=reduces_inflected_words(remove_all_stop_words(remove_all_punctuation(text1)))
    S1 = set(item for item in set(texta) if len(item) < 8)
    sets = generate_sets(S1)
    number_of_minhashes=10000
    # similarity=0.9
    b=197
    r=50
    threshold = (1 / b) ** (1 / r)
    similarity_rounded = round(threshold, 2)

    lsh = MinHashLSH(num_perm=number_of_minhashes,params=(b,r))

    for i in range(len(sets)):
        minhash = minhash_sign(sets[i],number_of_minhashes)
        lsh.insert(f'S{i+1}', minhash) 
    for i in range(len(sets)):
        minhash = minhash_sign(sets[i],number_of_minhashes)
        result = lsh.query(minhash)
        result = [elem for elem in result if elem != f'S{i+1}']
        if result!=[]:
            print("Approximate similar sets to S" + str(i+1) + " with Jaccard similarity > " + str(similarity_rounded) + " :" + str(result))   


