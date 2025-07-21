import nltk
nltk.download('book')
from nltk.book import text7
from nltk.book import text9

set_text7 = set(text7)
set_text9 = set(text9)

words_only_in_9 = set_text9 - set_text7


print("The set of words that appear in text9 but do not appear in text7")
print(words_only_in_9)