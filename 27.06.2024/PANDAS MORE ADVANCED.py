#Pandas is an open-source data manipulation and analysis library built on top of the Python programming language.
#It provides fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time-series data both easy and intuitive.
#It is a cornerstone for data analysis in Python, widely used in data science, machine learning, scientific computing, and many other fields.

#Key Data Structures
#Series:
#A one-dimensional labeled array capable of holding any data type (integers, strings, floating-point numbers, Python objects, etc.).
#The labels are known as the index.
import pandas as pd

# Creating a Series from a list
s = pd.Series([1, 3, 5, None, 6, 8])
print(s)

# Creating a Series from a dictionary
s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s)

#DataFrame:
#A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
#Can be thought of as a dictionary of Series objects
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]

df = pd.DataFrame(data)
print(df)

#Basic Operations:
#Indexing and Selecting Data:
#Selecting a column: You can select a column from a DataFrame using the column label.
ages = df['Age']
print(ages)

#Selecting rows by label: Use the loc attribute for label-based indexing:
row = df.loc[0]  
print(row)
rows = df.loc[0:1]  
print(rows)

#Filtering Data
#Filtering allows you to select rows that meet certain conditions.
# Selecting rows where Age > 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)

#Advanced Data Operations
#Grouping and Aggregation
#Grouping and aggregation are useful for summarizing data.
# Group by 'City' and calculate the mean of each group
grouped = df.groupby('City').mean()
print(grouped)

#Merging and Joining
#You can merge or join data from different DataFrames:
# Creating another DataFrame
data2 = {
    'Name': ['Alice', 'Bob', 'David'],
    'Salary': [50000, 60000, 70000]
}

df2 = pd.DataFrame(data2)

# Merging DataFrames on a common column
merged_df = pd.merge(df, df2, on='Name')
print(merged_df)

#Reshaping Data
#Pandas provides functions for reshaping data:
#Pivot: Reshape data where columns become rows and vice versa.
# Creating a sample DataFrame
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'City': ['New York', 'San Francisco', 'Los Angeles'],
    'Temperature': [30, 40, 50]
}

df = pd.DataFrame(data)

# Pivoting the DataFrame
pivoted_df = df.pivot(index='Date', columns='City', values='Temperature')
print(pivoted_df)

#Data Visualization
#Pandas integrates well with Matplotlib for data visualization:
import matplotlib.pyplot as plt

# Plotting a DataFrame
df.plot(kind='bar')
plt.show()


