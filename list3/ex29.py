import nltk
from nltk.book import text1
import list3

def remove_all_punctuation(text):
    text_without_punctuation=[]
    for item in text:
        if item.isalnum():
            text_without_punctuation.append(item)
    return text_without_punctuation 

lowercase = [word.lower() for word in text1]
text = remove_all_punctuation(lowercase)

def Hamming_dist(s1,s2):
    if len(s1) != len(s2):
        return 0
    ham_dist=0
    for elem1, elem2 in zip(s1,s2):              
            if elem1 != elem2:
                ham_dist += 1
    return ham_dist
 
if __name__ == "__main__":
    S=set(text)
    print("Diameter of metric space (text1,Hamming distance): ", list3.diameter(S,Hamming_dist))


