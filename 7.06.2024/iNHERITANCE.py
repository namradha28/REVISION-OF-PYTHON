INHERITANCE 
#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class (the child or subclass) to inherit attributes and methods from another class (the parent or superclass). This promotes code reuse and can simplify the structure of a program.
#KEY CONCEPTS OF INHERITANCE

#1.Superclass (Parent Class):
#The class whose attributes and methods are inherited.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This is a generic method that can be overridden by subclasses

#2.Subclass (Child Class):
#The class that inherits from the superclass.
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
--------------------------------------------------------------------------------------------------------------
#TYPES OF INHERITANCE:

#1.Single Inheritance:
#A subclass inherits from a single superclass.
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

#2.Multiple Inheritance:
#A subclass inherits from more than one superclass.
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Animal, Flyer, Swimmer):
    def speak(self):
        return f"{self.name} says Quack!"

#3.Multilevel Inheritance:
#A class is derived from a class that is also derived from another class.
class Canine(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Dog(Canine):
    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"

#4.Hierarchical Inheritance:
#Multiple subclasses inherit from a single superclass.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
#Using the super() Function:
#The super() function is used to call a method from the superclass. This is often used in the constructor to ensure that the superclass is properly initialized.
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Initialize the superclass
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"

dog = Dog("Rex", "German Shepherd")
print(dog.speak())  # Output: Rex the German Shepherd says Woof!

