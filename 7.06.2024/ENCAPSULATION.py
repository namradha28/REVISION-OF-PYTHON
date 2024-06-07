ENCAPSULATION 
#Encapsulation is a fundamental concept in object-oriented programming that binds together the data (attributes) and the functions (methods) that manipulate the data, and keeps both safe from outside interference and misuse. This means restricting direct access to some of an object's components, which can prevent the accidental modification of data.
#The bundling of data and methods that operate on the data within one unit, such as a class.
#It restricts direct access to some of the object's components, which is a way of preventing accidental interference and misuse of the data.

class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age

person = Person("John", 30)
print(person.get_name())  # Output: John

#In Python, we denote private attributes or methods by prefixing their names with double underscores (__). This makes them not accessible directly from outside the class.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
person.set_name("Bob")
print(person.get_name())  # Output: Bob

#Public methods are accessible from outside the class and are used to interface with the private attributes.

#DEMONSTRATING ENCAPSULATION
class Account:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

# Creating an account object
account = Account("John Doe", 1000)

# Accessing public methods
account.deposit(500)   # Output: Deposited 500. New balance is 1500.
account.withdraw(200)  # Output: Withdrew 200. New balance is 1300.
print(account.get_balance())  # Output: 1300
print(account.get_owner())    # Output: John Doe

# Direct access to private attributes will raise an error
# print(account.__balance)  # AttributeError
