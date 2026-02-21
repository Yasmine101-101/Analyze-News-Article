import re
from collections import Counter

def count_specific_word(text, word ):
    text = text.lower()
    word = word.lower()
    count = len(re.findall(r"\b" + word + r"\b", text))
    if count == 0:
        return 0

    return count

def identify_most_common_word(text):
    if not text:
        return None
    text = text.lower()
    word = re.findall(r"\b[a-z]+\b", text)
    word_count = Counter(word)
    most_common = word_count.most_common(1)[0][0]
    return most_common

def calculate_average_word_length(text):
    if not text:
        return 0
    words = re.findall(r"\b[a-z]+\b", text.lower())
    avarage = sum(len(word) for word in words) / len(words) 
    return float(avarage)

def count_paragraphs(text):
    if not text :
        return 1
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)
    
def count_sentences(str):
    pass

text = open("article.txt").read()
search_word = input("Enter the word you want to search for :  ")
result_word = count_specific_word(text, search_word)
print(f"The word {search_word} appears {result_word} times in the article.")

most_common_word = identify_most_common_word(text)
print(f"The most common word: {most_common_word} ")

avarage_lenght = calculate_average_word_length(text)
print(f"The avarage word lenght is :{avarage_lenght}")

paraghraph_count = count_paragraphs(text)
print(f"The number of paragraphs:{paraghraph_count}")