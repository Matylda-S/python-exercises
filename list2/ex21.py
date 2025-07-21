import nltk
nltk.download('book')
from nltk.book import text1
from nltk.book import text2
from nltk.book import text3
from nltk.book import text4
from nltk.book import text5
from nltk.book import text6
from nltk.book import text7
from nltk.book import text8
from nltk.book import text9


def remove_all_punctuation(text):
    text_without_punctuation=[]
    for item in text:
        if item.isalnum():
            text_without_punctuation.append(item)
    return text_without_punctuation   
 
table=[text1,text2,text3,text4,text5,text6,text7,text8,text9]
all_sets=[]
for item in table:
    item=remove_all_punctuation(item)
    all_sets.append(set(item))

common_words = set(all_sets[0])  
for s in all_sets[1:]:  
    common_words = common_words.intersection(s) 


print("Common words :")
print(common_words)
