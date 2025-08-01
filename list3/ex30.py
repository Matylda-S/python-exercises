import nltk
from nltk.book import text1
from list3 import set_jaccard
from nltk.tokenize import word_tokenize


def remove_all_punctuation(text):
    text_without_punctuation = []
    for item in text:
        if item.isalnum():
            text_without_punctuation.append(item)
    return text_without_punctuation 

dict = {}
lowercase = [word.lower() for word in text1]
text = remove_all_punctuation(lowercase)
count = len(text) - 1
for i in range(count):
    word1 = text[i]
    word2 = text[i + 1]
    x = set(word1)
    y = set(word2)
    dict[(word1, word2)] = set_jaccard(x, y)

for words, jaccard in dict.items():
    print("Words: ",words, ", Jaccard symilarity beetwen them: ", jaccard)

