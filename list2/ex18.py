from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def remove_all_punctuation(text):
    text_without_punctuation=[]
    for item in text:
        if item.isalnum():
            text_without_punctuation.append(item)
    return text_without_punctuation        

def remove_all_stop_words(text):
    words_stop=stopwords.words('english')
    text_without_stopwords=[]
    for item in text:
        item=item.lower()
        if item not in words_stop:
            text_without_stopwords.append(item)
    return text_without_stopwords

def reduces_inflected_words(text):
    stems=PorterStemmer()
    text_with_stems=[]
    for item in text:
        text_with_stems.append(stems.stem(item))
    return text_with_stems

def counted_and_sorted(text):
    words = {}
    for item in text:
        if item in words:
            words[item] += 1
        else:
            words[item] = 1
    words_over_100=[]
    for word, count in words.items():  
        if count >= 100: 
            words_over_100.append(word) 
    words_over_100.sort()
    return words_over_100


with open('hamlet.txt', 'r', encoding='utf-8') as file:
    hamlet_text = file.read()

text=word_tokenize(hamlet_text)
text=remove_all_punctuation(text)
text=remove_all_stop_words(text)
text=reduces_inflected_words(text)
words_over_100=counted_and_sorted(text)       
print(words_over_100)       

