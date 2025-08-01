from collections import Counter
from nltk.book import text1, text2, text3, text4, text5, text6, text7, text8, text9
from list3 import bag_jaccard
def remove_all_punctuation(text):
    text_without_punctuation=[]
    for item in text:
        if item.isalnum():
            text_without_punctuation.append(item)
    return text_without_punctuation 

if __name__ == "__main__":
    all_texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]

    all_texts = [' '.join(remove_all_punctuation(item)) for item in all_texts]



    for i, item in enumerate(all_texts):
        for item2 in all_texts[i+1:]:
            jaccard_sym =bag_jaccard(item, item2)
            print("Jaccard Similarity between texts:text{} and text{}: {}".format(i+1, all_texts.index(item2) + 1, jaccard_sym))


