ABSTRACTION 

#Abstraction is a fundamental concept in object-oriented programming (OOP) that focuses on hiding the complex implementation details and showing only the essential features of an object. It helps in reducing complexity by allowing the programmer to manage complexity through simplified models and interfaces. In Python, abstraction can be achieved using abstract classes and interfaces
#The concept of hiding the complex implementation details and showing only the necessary features of an object.
#In Python, it is often achieved using abstract classes and methods.

#DEFINING AN ABSTRACT CLASS 
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
#Implementing Abstract Methods in Subclasses:
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

#DEMONSTRATING ABSTRACTION 
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

    def stop_engine(self):
        return "Motorcycle engine stopped"

# Creating objects of the subclasses
car = Car()
motorcycle = Motorcycle()

print(car.start_engine())      # Output: Car engine started
print(car.stop_engine())       # Output: Car engine stopped
print(motorcycle.start_engine())  # Output: Motorcycle engine started
print(motorcycle.stop_engine())   # Output: Motorcycle engine stopped
