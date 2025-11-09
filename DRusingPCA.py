import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

doc=[
    "CUTM is  located in paralakhemundi",
    "paralakhemundi is  located in Odisha",
    "Odisha is a state"
]

tfidf= TfidfVectorizer()
X = tfidf.fit_transform(doc)
words = tfidf.get_feature_names_out(doc)
print (words)
print("\n", X, "\n")

print(X.shape, "\n")





#Eigenn val,vec, cav, mean
X_centered= X - X.mean(axis=0)

print(X_centered, "\n")
cov=np.cov(X_centered, rowvar=False)
print("\n", cov)