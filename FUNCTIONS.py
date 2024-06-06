FUNCTIONS

#Functions are reusable blocks of code that perform a specific task.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#There are two types of functions:
#**Built-in library function: These are Standard functions in Python that are available to use.
#**User-defined function: We can create our own functions based on our requirements.

#Built-in functions: There are many build-in-functions like len(),max(),min(),type(),etc...
#len()- Gives the length of the string 
#min()- Gives the minimum number in a particular list. 
#max()- Gives the maximum number in a particular list   

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5
#Functions are reusable blocks of code that perform a specific task.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#There are two types of functions:
#**Built-in library function: These are Standard functions in Python that are available to use.
#**User-defined function: We can create our own functions based on our requirements.

#Built-in functions: There are many build-in-functions like len(),max(),min(),type(),etc...
#len()- Gives the length of the string 
#min()- Gives the minimum number in a particular list. 
#max()- Gives the maximum number in a particular list   

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

numbers = [10, 20, 30, 40, 50]
print(max(numbers))  # Output: 50

x = 42
print(type(x))    # Output: 50

x = 42
print(type(x))  

#User-defined functions: User-defined functions are created by users to perform specific tasks. You define a function using the def keyword followed by the function name and parentheses ().
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())        # Output: Hello, Guest!
print(greet("Bob"))   # Output: Hello, Bob!




