from nltk.book import text8
from nltk.stem import PorterStemmer
from list3 import levenshtein
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

if __name__ == "__main__":

    lowercase = [word.lower() for word in text8]
    words = list(set(reduces_inflected_words(remove_all_punctuation(lowercase))))
    min_dist= 10000000
    word1=''
    word2=''

    for i,item in enumerate(words):
        for item2 in words[i+1:]:
            dist=levenshtein(item,item2)/(len(item)+len(item2))
            if dist<min_dist:
                min_dist=dist
                word1=item
                word2=item2

    print("Pair of words with minimal relative edit distance: {}, {}, distance between them: {}".format(word1, word2, min_dist))              

     

