from sklearn import datasets
import seaborn as sns
import pandas as pd

# Load dataset

iris=datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2)

from sklearn.neighbors import  KNeighborsClassifier
knn=KNeighborsClassifier()

train=knn.fit(x_train, y_train)
y_pred=knn.predict(x_test)

print(y_pred)