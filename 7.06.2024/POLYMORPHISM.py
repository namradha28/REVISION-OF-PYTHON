POLYMORPHISM 

#Polymorphism is a key concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It provides a way to perform a single action in different forms. Polymorphism allows for methods to be used interchangeably, even if the specific implementation of the method differs between classes.
#TYPES OF POLYMORPHISM:
#Compile-Time Polymorphism (Method Overloading):
#Python does not support method overloading in the traditional sense found in some other languages like Java or C++. However, you can achieve a similar effect using default arguments or variable-length arguments.
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math_op = MathOperations()
print(math_op.add(2, 3))    # Output: 5
print(math_op.add(2, 3, 4)) # Output: 9

#Runtime Polymorphism (Method Overriding):
#This occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method to be called is determined at runtime based on the object type.
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!

#DEMONSTRATING POLYMORPHISM
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

shapes = [Rectangle(2, 3), Circle(5)]

for shape in shapes:
    print(f"The area is: {shape.area()}")
