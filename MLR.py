import seaborn as sns
import pandas as pd

# Load dataset
df = sns.load_dataset("iris")

# View 
print(df)
import numpy as np
x = df[['sepal_length', 'sepal_width']]
y = df.petal_length

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

from sklearn.linear_model import LinearRegression
LR= LinearRegression()

training = LR.fit(x_train, y_train)
y_pred = LR.predict(x_test)
print(y_pred)