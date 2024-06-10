Dictionary 

#A dictionary in Python is an unordered collection of items. Each item is a pair consisting of a key and a value. Dictionaries are optimized for retrieving values when the key is known.
 #Creating Dictionaries
#You can create dictionaries using curly braces {} with key-value pairs separated by a colon :.
# An empty dictionary
empty_dict = {}

# A dictionary with integer keys
int_key_dict = {1: "apple", 2: "banana", 3: "cherry"}

# A dictionary with string keys
str_key_dict = {"name": "Alice", "age": 25, "city": "New York"}

# A dictionary with mixed keys
mixed_key_dict = {1: "apple", "name": "Alice", 3.14: "pi"}

# A nested dictionary
nested_dict = {"person": {"name": "Alice", "age": 25}, "city": "New York"}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Accessing Dictionary Values
#You can access dictionary values by using their keys.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 25

# Accessing nested values
nested_dict = {"person": {"name": "Alice", "age": 25}, "city": "New York"}
print(nested_dict["person"]["name"])  # Output: Alice
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Dictionary Methods
#Dictionaries come with several built-in methods for various operations.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# keys() returns a view object of the dictionary's keys
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# values() returns a view object of the dictionary's values
values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 25, 'New York'])

# items() returns a view object of the dictionary's key-value pairs
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# get() returns the value for a specified key, if the key is in the dictionary
name = my_dict.get("name")
print(name)  # Output: Alice

# setdefault() returns the value of a key if it is in the dictionary; otherwise, it inserts the key with a specified value
city = my_dict.setdefault("city", "Unknown")
print(city)   # Output: New York
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# update() updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs
my_dict.update({"age": 26, "email": "alice@example.com"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# clear() removes all items from the dictionary
my_dict.clear()
print(my_dict)  # Output: {}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Iterating Over Dictionaries
#You can iterate over dictionaries using loops.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])
# Output:
# name Alice
# age 25
# city New York

# Iterating over values
for value in my_dict.values():
    print(value)
# Output:
# Alice
# 25
# New York

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)
# Output:
# name Alice
# age 25
# city New York
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Dictionary Functions
#Python provides several built-in functions that operate on dictionaries.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# len() returns the number of items in the dictionary
print(len(my_dict))  # Output: 3

# sorted() returns a sorted list of the dictionary's keys
sorted_keys = sorted(my_dict)
print(sorted_keys)  # Output: ['age', 'city', 'name']

# max() returns the maximum key
print(max(my_dict))  # Output: name

# min() returns the minimum key
print(min(my_dict))  # Output: age



