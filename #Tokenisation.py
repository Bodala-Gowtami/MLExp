#Tokenisation
input = "Barack Obama is a prime minister of USA in the year of 2015."
print(input)
lowercase = input.lower()
from nltk import word_tokenize, sent_tokenize
word_tokens = word_tokenize(lowercase)
print(word_tokens)