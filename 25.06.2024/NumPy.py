#NumPy is a powerful library in Python that is used for numerical and scientific computing.
#  It provides support for large multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

#You can install NumPy using pip:
pip install numpy

#Importing NumPy
import numpy as np

#Creating Arrays
# 1. From a list:
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#2. Multi-dimensional array:
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# 3. Arrays with zeros, ones, or a range of values:
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
range_arr = np.arange(0, 10, 2)

# Indexing and Slicing
# 1. Indexing:

arr = np.array([1, 2, 3, 4, 5])
print(arr[0]) 

#2. Slicing:

print(arr[1:4])  
#3. Multi-dimensional indexing and slicing:
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d[0, 1])  
print(arr_2d[:, 1])  
#Reshaping Arrays
#1. Reshape:
arr = np.arange(8)
reshaped = arr.reshape((2, 4))
print(reshaped)

#2. Flatten:
flattened = reshaped.flatten()
print(flattened)

#Aggregation Functions
#1. Sum, mean, max, min:
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))  
print(np.mean(arr))  
print(np.max(arr))  
print(np.min(arr))  

#2. Axis-specific operations:
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr_2d, axis=0))  # Output: [5 7 9]
print(np.sum(arr_2d, axis=1))  # Output: [ 6 15]

#Broadcasting
#1. Broadcasting example
arr = np.array([1, 2, 3])
arr_2d = np.array([[1], [2], [3]])

result = arr + arr_2d
print(result)

#Linear Algebra
#1. Dot product:

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

dot_product = np.dot(a, b)
print(dot_product)

#2. Transpose:
a = np.array([[1, 2], [3, 4]])
print(a.T)

#Random Numbers
#1. Generating random numbers:


rand_arr = np.random.rand(2, 3) 
rand_int = np.random.randint(0, 10, (2, 3)) 
