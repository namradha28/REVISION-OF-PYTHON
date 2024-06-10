Tuples 

#Tuples in Python are ordered, immutable collections of items. Unlike lists, once a tuple is created, its elements cannot be changed, which makes tuples useful for data that should not be modified.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CREATING A TUPLE 
#Tuples can be created by using ()
# An empty tuple
empty_tuple = ()
# A tuple with integers
int_tuple = (1, 2, 3, 4, 5)
# A tuple with strings
str_tuple = ("apple", "banana", "cherry")
# A mixed data type tuple
mixed_tuple = (1, "apple", 3.14, True)
# A nested tuple
nested_tuple = (1, (2, 3), (4, 5))
# A tuple without parentheses (implicit tuple)
implicit_tuple = 1, 2, 3
#ACCESING TUPLE ELEMENTS 
my_tuple = ("apple", "banana", "cherry")
# Access the first element
print(my_tuple[0])  # Output: apple
# Access the last element
print(my_tuple[-1])  # Output: cherry
# Access elements in a nested tuple
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1][1])  # Output: 3
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#IMMUTABLILITY 
my_tuple = (1, 2, 3)

# Attempt to change an element
try:
    my_tuple[0] = 10
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
#Tuples are immutable, meaning once they are created, their elements cannot be changed. Any attempt to modify a tuple results in an error.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Tuple Operations
#Tuples support various operations similar to lists, but they do not support item assignment.
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3
print(repeated)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership test
print(3 in tuple1)  # Output: True
print(7 in tuple1)  # Output: False

# Length
print(len(tuple1))  # Output: 3

# Minimum and Maximum
print(min(tuple1))  # Output: 1
print(max(tuple1))  # Output: 3

# Sum
print(sum(tuple1))  # Output: 6
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Iterating Over Tuples
#You can iterate over tuples using loops.
my_tuple = ("apple", "banana", "cherry")

# Using a for loop
for fruit in my_tuple:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Using a while loop
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1
# Output:
# apple
# banana
# cherry
