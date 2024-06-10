SETS
#Sets in Python are collections of unique and unordered elements. They are useful when you need to store non-duplicate items and perform common set operations such as union, intersection, and difference.
#CREATING SETS 
#You can create sets using curly braces {} or the set() function.
# An empty set
empty_set = set()

# A set with elements
fruit_set = {"apple", "banana", "cherry"}

# Using the set() function
num_set = set([1, 2, 3, 4])

'''Characteristics of Sets
Unordered: The elements have no specific order.
Unique: Duplicate elements are automatically removed.
Mutable: Elements can be added or removed.'''

#Adding and Removing Elements
#You can add elements using the add() method and remove them using the remove() or discard() methods.
my_set = {1, 2, 3}

# Add an element
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Remove an element
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Discard an element (no error if element does not exist)
my_set.discard(5)
print(my_set)  # Output: {1, 3, 4}

# Remove and return an arbitrary element
removed_element = my_set.pop()
print(removed_element)  # Output: 1 (or any other element, since sets are unordered)
print(my_set)  # Output: {3, 4} (or remaining elements)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Set Operations
#Sets support various mathematical set operations such as union, intersection, difference, and symmetric difference.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: elements in either set
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection: elements in both sets
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

# Difference: elements in set1 but not in set2
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# Symmetric Difference: elements in either set, but not both
sym_diff_set = set1 ^ set2
print(sym_diff_set)  # Output: {1, 2, 4, 5}
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Iterating Over Sets
#You can iterate over a set using a for loop.
my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)
# Output:
# apple
# banana
# cherry
