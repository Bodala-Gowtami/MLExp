import pandas as pd
from sklearn import datasets

# Load iris dataset
iris = datasets.load_iris()

# Create a DataFrame from the data
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target column to the DataFrame
df['target'] = iris.target

# Now use iloc to extract X and y
x = df.iloc[:, :-1].values  # All rows, all columns except last
y = df.iloc[:, -1].values   # All rows, last column only

print(x)
print(y)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2)


from sklearn.cluster import KMeans
KMeans = KMeans(n_clusters = 3)
y_pred=KMeans.fit_predict(x)
print(y_pred)


import matplotlib.pyplot as plt
plt.scatter(x[y_pred == 0,0], x[y_pred == 0,1], s=50, c='red', label = 'setosa')
plt.scatter(x[y_pred == 1,0], x[y_pred == 1,1], s=50, c='blue', label = 'versicolor')
plt.scatter(x[y_pred == 2,0], x[y_pred == 2,1], s=50, c='green', label = 'verginica')
plt.scatter(KMeans.cluster_centers_[:,0],KMeans.cluster_centers_[:,1], s=150, c='yellow', label = 'centroid')
plt.legend()
plt.title("KMeans Clustering on Iris Data")
plt.show()