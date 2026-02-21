import re
from collections import Counter

def count_specific_word(text, word ):
    text = text.lower()
    word = word.lower()
    count = len(re.findall(r"\b" + word + r"\b", text))
    return count

def identify_most_common_word(text):
    if not text:
        return None
    text = text.lower()
    word = re.findall(r"\b[a-z]+\b", text)
    word_count = Counter(word)
    most_common = word_count.most_common(1)[0][0]
    return most_common

def calculate_average_word_length(str):
    pass
def count_paragraphs(str):
    pass
def count_sentences(str):
    pass

text = open("article.txt").read()
search_word = input("Enter the word you want to search for :  ")
result_word = count_specific_word(text, search_word)
print(f"The word {search_word} appears {result_word} times in the article.")

most_common_word = identify_most_common_word(text)
print(f"The most common word: {most_common_word} ")