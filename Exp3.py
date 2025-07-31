import nltk
from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize
input = "Barack Obama is a prime minister of USA in the year of 2015. PM modi is the P M of INDIA."
#print(len(sent_tokenize(input)))
ner = ne_chunk(pos_tag(word_tokenize(input)))
#print(ner) ## S in the  output represented as ROOT


import spacy
from nltk.tree import Tree
named_entity = []
for subtree in ner:
    if isinstance(subtree, Tree):
        entity = " ".join([token for token, pos in subtree.leaves()])
        named_entity.append(entity)
print(named_entity)
nlp = spacy.load("en_core_web_sm")
text = "Barack Obama is a prime minister of USA in the year of 2015. PM modi is the P M of INDIA."
doc = nlp(text)
named_entity = []
for ent in doc.ents:
    named_entity.append(ent.text)
print(named_entity)