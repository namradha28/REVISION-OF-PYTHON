CLASSES AND OBJECTS
#In Python, a class is a blueprint for creating objects (instances). A class defines a set of attributes and methods that the created objects can use. An object is an instance of a class, created with specific data.
#SIMPLE CLASS 
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
#CREATING AN OBJECT 
my_dog = Dog("Rex", 5)
print(my_dog.name)  # Output: Rex
print(my_dog.age)   # Output: 5
print(my_dog.species)  # Output: Canis familiaris
print(my_dog.bark())   # Output: Rex says woof!

#Class and Instance Attributes
#Class attributes are shared among all instances of a class. They are defined directly within the class.
#Instance attributes are unique to each instance and are defined within the __init__ method.
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.wheels)  # Output: 4 (class attribute)
print(my_car.make)    # Output: Toyota (instance attribute)
print(my_car.model)   # Output: Corolla (instance attribute)

#Methods
#Methods are functions defined within a class that operate on instances of that class. There are three types of methods in Python:
#Instance Methods: Operate on an instance of the class.
#Class Methods: Operate on the class itself, not instances. Use the @classmethod decorator.
#Static Methods: Do not operate on either class or instance. Use the @staticmethod decorator.

class Circle:
    # Class attribute
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # Instance method
    def area(self):
        return Circle.pi * (self.radius ** 2)

    # Class method
    @classmethod
    def circumference(cls, radius):
        return 2 * cls.pi * radius

    # Static method
    @staticmethod
    def info():
        return "This is a circle class"

circle = Circle(5)
print(circle.area())                     # Output: 78.5
print(Circle.circumference(5))           # Output: 31.400000000000002
print(Circle.info())                     # Output: This is a circle class
