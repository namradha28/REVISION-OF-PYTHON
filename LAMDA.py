LAMDA
#A lambda function in Python is a small, anonymous function that is defined without a name. It's often used for simple, one-time tasks that are not complex enough to require a full function definition.
#Key Points
#Anonymous: Lambda functions do not need a name.
#Single Expression: They can only contain a single line of code.
#Quick to Write: Ideal for simple operations where writing a full function would be too much.

#ADDING 2 NUMBERS 
def add(x, y):
    return x + y

print(add(2, 3))  # Output: 5

#USING MAP FUNCTION
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8]

#USING FILTER FUNCTION
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

