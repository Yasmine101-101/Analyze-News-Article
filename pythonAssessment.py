import re

def count_specific_word(text, word ):
    text = text.lower()
    word = word.lower()
    count = len(re.findall(r"\b" + word + r"\b", text))
    return count
text = open("article.txt").read()
search_word = input("Enter the word you want to search for :  ")
result_word = count_specific_word(text, search_word)
print(f"The word {search_word} appears {result_word} times in the article.")

    
def identify_most_common_word(str):
    pass
def calculate_average_word_length(str):
    pass
def count_paragraphs(str):
    pass
def count_sentences(str):
    pass