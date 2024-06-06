VARIABLES AND DATA TYPES 

#Python variables are the reserved memory locations used to store values with in a Python Program.
#Integer 
a=10
print(a)
#Float 
b=(5.0)
print(b)
#String 
c='I am Namradha'
print(c)
#Boolean
d=True 
print(d)

#LISTS
a=[10,20,30,20,40,50]
print(a[2])
#List is mutable and can be traversed using its index value
a.append(80)
print(a) #This is used to add an element at the end of the list 
a.remove(20)
print(a) #This is used to remove an element from the list
#Collection of ordered and changebale. It allows duplicate values.

#TUPLES 
b=(10,20,30,40,50)
print(b(2))
#Tuples are immutable. It cannot be changed.

#Dictionaries 
# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25}
# Accessing values
print(my_dict['name'])
# Modifying values
my_dict['age'] = 26
print(my_dict)
# Adding a new key-value pair
my_dict['city'] = 'New York'
print(my_dict)

