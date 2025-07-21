import nltk
nltk.download('book')
from nltk.book import text2
from nltk.tokenize import sent_tokenize


def remove_hyphen(text):
    hyphen='.--'
    text_without_stopwords=[]
    for item in text:
        if item ==hyphen :
            item='.'
            text_without_stopwords.append(item)
        elif item=='?--':
            item='?'
            text_without_stopwords.append(item)   
        else :
            text_without_stopwords.append(item)    
    return text_without_stopwords

a=remove_hyphen(text2)
text = ' '.join(a)

sentences = sent_tokenize(text)
longest_sentence = max(sentences, key=len)


print("The longest sentence in Jane Austen’s Sense and Sensibility:")
print(longest_sentence)


