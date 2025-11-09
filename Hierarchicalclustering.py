import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# -----------------------
# 1. Plot Dendrogram
# -----------------------
linked = linkage(X, method='ward')

plt.figure(figsize=(10, 6))
dendrogram(linked,
           orientation='top',
           distance_sort='descending',
           show_leaf_counts=False)
plt.title("Hierarchical Clustering Dendrogram (Iris)")
plt.xlabel("Samples")
plt.ylabel("Euclidean distance")
plt.show()


# -----------------------
# 2. Apply Agglomerative Clustering
# -----------------------
agg = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
y_pred = agg.fit_predict(X)

# -----------------------
# 3. Plot Clusters in 2D
# -----------------------
plt.figure(figsize=(8,6))
plt.scatter(X[y_pred == 0, 0], X[y_pred == 0, 1], c='red', label='setosa')
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], c='blue', label='versicolor')
plt.scatter(X[y_pred == 2, 0], X[y_pred == 2, 1], c='green', label='virginica')

plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.title("Agglomerative Clustering on Iris (2D)")
plt.legend()
plt.show()
