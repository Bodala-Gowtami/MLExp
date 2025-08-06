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


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
Accuracy = accuracy_score(y_test, y_pred)
Precision=precision_score(y_test, y_pred, average='macro')
Recall=recall_score(y_test, y_pred, average='macro')
f1= f1_score(y_test, y_pred, average='macro')

print("\nAccuracy : ", Accuracy)
print("Precision : ", Precision)
print("\nAccuracy : ", Recall)
print("\nF1_Score : ", f1)