from nltk.book import text1
from list3 import levenshtein

def remove_all_punctuation(text):
    text_without_punctuation=[]
    for item in text:
        if item.isalnum():
            text_without_punctuation.append(item)
    return text_without_punctuation 

if __name__ == "__main__":
    word_dog = "dog"

    all_words = []
    lowercase = [word.lower() for word in text1]
    text=set(remove_all_punctuation(lowercase))
    for item in set(text):
        if abs(len(item)- len(word_dog))<4:
            levenshtein_dist = levenshtein(item, word_dog)
            if levenshtein_dist < 4:
                all_words.append(item)

    print("All words with Levenshtein distance between them and the word dog smaller than 4:", all_words)