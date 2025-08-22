from list3 import set_jaccard
from nltk.book import text1,text2,text3
from datasketch import MinHash
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
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

if __name__ == "__main__":
    texta=reduces_inflected_words(remove_all_stop_words(remove_all_punctuation(text1)))
    textb=reduces_inflected_words(remove_all_stop_words(remove_all_punctuation(text2)))
    textc=reduces_inflected_words(remove_all_stop_words(remove_all_punctuation(text3)))

    S1 = set(item for item in set(texta) if len(item) < 8)
    S2 = set(item for item in set(textb) if len(item) < 8)
    S3 = set(item for item in set(textc) if len(item) < 8)

    minhash_S1 = MinHash(100)
    minhash_S2 = MinHash(100)
    minhash_S3 = MinHash(100)


    for item in S1:
        item=item.encode('utf8')
        minhash_S1.update(item)
    for item in S2:
        item=item.encode('utf8')
        minhash_S2.update(item)
    for item in S3:
        item=item.encode('utf8')
        minhash_S3.update(item)


    print("Estimated Jaccard similarity between text1 and text2:", minhash_S1.jaccard(minhash_S2))
    print("Exact Jaccard similarity between text1 and text2:", set_jaccard(S1,S2))
    print("Difference:", abs(set_jaccard(S1,S2) -minhash_S1.jaccard(minhash_S2)))
    print("Estimated Jaccard similarity between text2 and text3:", minhash_S2.jaccard(minhash_S3))
    print("Exact Jaccard similarity between text2 and text3:", set_jaccard(S2,S3))
    print("Difference:", abs(set_jaccard(S2,S3) -minhash_S2.jaccard(minhash_S3)))
    print("Estimated Jaccard similarity between text1 and text3:", minhash_S1.jaccard(minhash_S3))
    print("Exact Jaccard similarity between text1 and text3:", set_jaccard(S1,S3))
    print("Difference:", abs(set_jaccard(S1,S3) -minhash_S1.jaccard(minhash_S3)))
