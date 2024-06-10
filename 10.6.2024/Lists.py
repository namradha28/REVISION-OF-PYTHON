Lists 

#Lists in Python are ordered collections that allow you to store and manipulate a sequence of items. They are versatile and can contain items of different types, including other lists. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREATE A LIST 
# An empty list
empty_list = []
# A list of integers
int_list = [1, 2, 3, 4, 5]
# A list of strings
str_list = ["apple", "banana", "cherry"]
# A mixed list
mixed_list = [1, "apple", 3.14, True]
# A nested list
nested_list = [1, [2, 3], [4, 5]]
---------------------------------------------------------------------------------------------------------------------------------------------------
#ACCESSING ELEMENTS 
my_list = ["apple", "banana", "cherry"]
# Access the first element
print(my_list[0])  # Output: apple
# Access the last element
print(my_list[-1])  # Output: cherry
# Access elements in a nested list
nested_list = [1, [2, 3], [4, 5]]
print(nested_list[1][1])  # Output: 3
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#LIST METHODS 
my_list = [1, 2, 3]
# Add an element at the end
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
# Add multiple elements
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
# Insert an element at a specific position
my_list.insert(1, 10)
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6]
# Remove the first occurrence of an element
my_list.remove(10)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
# Remove and return an element at a specific position
element = my_list.pop(1)
print(element)  # Output: 2
print(my_list)  # Output: [1, 3, 4, 5, 6]
# Get the index of the first occurrence of an element
index = my_list.index(4)
print(index)  # Output: 2
# Count the occurrences of an element
count = my_list.count(3)
print(count)  # Output: 1
# Sort the list
my_list.sort()
print(my_list)  # Output: [1, 3, 4, 5, 6]
# Reverse the list
my_list.reverse()
print(my_list)  # Output: [6, 5, 4, 3, 1]
# Clear the list
my_list.clear()
print(my_list)  # Output: []
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ITERATING LISTS 
my_list = ["apple", "banana", "cherry"]

# Using a for loop
for fruit in my_list:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Using a while loop
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
# Output:
# apple
# banana
# cherry
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Python lists are a fundamental and powerful tool for managing collections of items. Their flexibility in terms of data types, dynamic nature, and extensive built-in methods make them suitable for a wide range of applications. Understanding how to effectively









