import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the Dataset
data = pd.read_csv(r"C:\Users\gowta\Downloads\housepredictiondataset\Bengaluru_House_Data.csv")

# Step 3: Initial Data Exploration
print(data.head(10))
print(data.info())

# Step 4: Data Cleaning Techniques
# Create a working copy
df = data.copy()

# 4.1 Handle Missing Values
# Print columns with missing values
print("\nMissing values before handling:\n", df.isnull().sum())

# Fill numeric missing values
if 'price' in df.columns:
    df['price'].fillna(df['price'].median(), inplace=True)

# Fill categorical missing values
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing values after filling:\n", df.isnull().sum())

# 4.2 Handle Duplicate Values
duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_count}")
df.drop_duplicates(inplace=True)
print(f"Data shape after removing duplicates: {df.shape}")

# 4.3 Drop remaining nulls if any
print("\nNull values before dropping:\n", df.isnull().sum())
df.dropna(inplace=True)
print(f"Shape after dropping nulls: {df.shape}")
print("Null values after dropping:\n", df.isnull().sum())

# 4.4 Handle Outliers in Price
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter rows within the IQR range
df = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]
print(f"\nData shape after removing outliers: {df.shape}")
