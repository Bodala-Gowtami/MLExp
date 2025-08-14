import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 2: Load the Dataset
data = pd.read_csv(r"C:\Users\gowta\Downloads\housepredictiondataset\Bengaluru_House_Data.csv")

#Step 3: Initial Data Exploration
data.head(10)
data.info()

df = data.copy()
#Step 4: Data Transformation Techniques
 #4.1  Normalization Technique
from sklearn.preprocessing import MinMaxScaler
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
scaler = MinMaxScaler()
df_normalized = df.copy()
df_normalized[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print(df_normalized[numeric_cols].head())

#4.2 Scaling Technique 
from sklearn.preprocessing import RobustScaler
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
scaler = RobustScaler()
df_scaled = df.copy()
df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print(df_scaled[numeric_cols].head())

#4.3 Standardization Technique 
from sklearn.preprocessing import StandardScaler
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
df_standardized = df.copy()
df_standardized[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print(df_standardized[numeric_cols].head())

