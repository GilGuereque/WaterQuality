import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

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

# Save the DataFrame to a table in the database
df.to_sql('water_quality', connection, if_exists='replace', index=False)

# Visualizing Distribution before standardization
# List of numerical columns to visualize (excluding Potability)
columns_to_visualize = ["ph", "Hardness", "Solids", "Chloramines", "Sulfate", "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"]

# Set up the figure size
plt.figure(figsize=(12, 8))

# Plot a histogram for each numerical column
for i, col in enumerate(columns_to_visualize, 1):
    plt.subplot(3, 3, i) # 3x3 grid of subplots
    sns.histplot(df[col], bins=30, kde=True) # Histogram with 30 bins and a kernel density estimate
    plt.title(f"Distributions of {col} (Before Standardization)")

plt.tight_layout()
plt.show()

# Create the scaler
scaler = StandardScaler()  

df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])  # Apply scaling to all features except Potability

# Visualizing Distribution after standardization
# Set up the figure size
plt.figure(figsize=(12, 8))

# Plot a histogram for each numerical column
for i, col in enumerate(columns_to_visualize, 1):
    plt.subplot(3, 3, i) # 3x3 grid of subplots
    sns.histplot(df[col], bins=30, kde=True) # Histogram with 30 bins and a kernel density estimate
    plt.title(f"Distributions of {col} (After Standardization)")

plt.tight_layout()
plt.show()

## TODO: Load the dataset into PowerBI and build some visualizations ?
## Save the cleaned data to a new CSV file