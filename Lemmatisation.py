input = "Barack Obama is a prime minister of USA in the year of 2015."
print(input)
# lowercase
lowercase = input.lower()
print(lowercase)
print("LOWERCASE = ", lowercase)

#re

#pip install re
import re #Regular Expression
lowercase_re = re.sub('2015', '2025', lowercase)
print("REGULAR EXP1 = ",lowercase_re)
lowercase_re = re.sub('[a-i]', '*', lowercase)
print("REGULAR EXP2 = ",lowercase_re)
lowercase_re = re.sub('\d', '-', lowercase)
print("REGULAR EXP3 = ",lowercase_re)

#Tokenisation
from nltk import word_tokenize, sent_tokenize
word_tokens = word_tokenize(lowercase)
print(word_tokens)

from  nltk.corpus import  stopwords
print(stopwords.fileids())
stopwords = set(stopwords.words('english'))
#print("\n", stopwords)
print("\n")

tokens_stopwords = []
for token in word_tokens:
    if token not in stopwords:
       tokens_stopwords.append(token)
print(tokens_stopwords)
print("\n")
print(''.join(tokens_stopwords))
print("\n")
print(' '.join(tokens_stopwords))

#Stemmer
stemming = []
from nltk import PorterStemmer
for word in tokens_stopwords:
    stemming.append(PorterStemmer().stem(word))
    print(stemming)

#lemmatizer
from nltk import WordNetLemmatizer
lma = []
for word in tokens_stopwords:
    lma.append(WordNetLemmatizer().lemmatize(word))
print(lma)


## creatiing lemmatin function