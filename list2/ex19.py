import nltk
nltk.download('book')
from nltk.book import text9
from nltk.stem import PorterStemmer
from nltk.book import text7

def counted_all_stems(text,word):
    stems=PorterStemmer()
    text_with_stems=[]
    for item in text:
        text_with_stems.append(stems.stem(item))
    counter=0
    for item in text_with_stems:
        if item == word.lower():
            counter += 1
    return counter


print("Number of occurrences of the word 'Sunday' in 'The Man Who Was Thursday: A Nightmare':", text9.count('Sunday'))
print("Number of occurrences of the word 'Sunday' in 'The Wall Street Journal':",text7.count('Sunday'))
print("Number of occurrences of the word 'Sunday' in all forms in 'The Man Who Was Thursday: A Nightmare':", counted_all_stems(text9,'Sunday'))
print("Number of occurrences of the word 'Sunday' in all forms in 'The Wall Street Journal':", counted_all_stems(text7,'Sunday'))