import pandas as pd
import sqlite3

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('./.data/water_potability.csv')

print(df.head())

df["ph"].fillna(df["ph"].median(), inplace=True) # Handle outliers

print(df.head())

df["Sulfate"].fillna(df["Sulfate"].mean(), inplace=True) # Handle outliers

df["Trihalomethanes"].fillna(df["Trihalomethanes"].median(), inplace=True) # Handle outliers

print(df.head())

df.to_csv('./.data/water_potability_cleaned.csv', index=False)

connection = sqlite3.connect('./.data/water_quality.db')


