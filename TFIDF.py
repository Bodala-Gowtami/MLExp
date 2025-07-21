
# TF-IDF
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
vector = TfidfVectorizer()

documents= [ "apple boy cat", "apple cat dog", "dog egg fan" ]

preprocessed = []
for doc in documents:
    tokenization = word_tokenize(doc)
    stop = [ps.stem(word) for word in tokenization if word not in stop_words]
    preprocessed.append(" ".join(stop))
print("Preprocessed documents:", preprocessed)
tfidf_matrix = vector.fit_transform(preprocessed)
print("TF-IDF Matrix (as array):\n", tfidf_matrix.toarray())
print("Feature names:", vector.get_feature_names_out())