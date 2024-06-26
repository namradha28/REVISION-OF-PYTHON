#Pandas is a powerful and widely-used open-source data manipulation and analysis library for Python.
#  It provides data structures and functions needed to work with structured data seamlessly and efficiently.

#Importing Pandas
import pandas as pd

#Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)


# Reading data from a CSV file
df = pd.read_csv('data.csv')

# Writing data to a CSV file
df.to_csv('output.csv', index=False)

#DATA MANIPULATION 
# Selecting a column
ages = df['Age']

# Filtering rows based on a condition
filtered_df = df[df['Age'] > 30]

# Grouping and aggregating data
grouped = df.groupby('City').mean()

# Handling missing data
df = df.dropna()  # Drop rows with any missing values
df = df.fillna(0)  # Fill missing values with 0


#WORKING WITH PANDAS IN A TIME SERIES
# Creating a date range
rng = pd.date_range('2024-01-01', periods=10, freq='D')
print(rng)

# Creating a DataFrame with a time index
ts = pd.Series(np.random.randn(10), index=rng)
print(ts)

#Basic Operations:
#Indexing and Selecting Data
#Selecting a column: You can select a column from a DataFrame using the column label.
ages = df['Age']
print(ages)

#Selecting rows by label: Use the loc attribute for label-based indexing.
row = df.loc[0]  # First row
print(row)

rows = df.loc[0:1]  # First two rows
print(rows)

#Filtering Data
#Filtering allows you to select rows that meet certain conditions.
# Selecting rows where Age > 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)

#Visualization
#Pandas integrates with Matplotlib for data visualization:
import matplotlib.pyplot as plt

# Plotting a DataFrame
df.plot(kind='bar')
plt.show()


