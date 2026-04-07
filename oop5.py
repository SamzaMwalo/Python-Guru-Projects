"""
Object Oriented Programming - Abstraction
Abstraction -> shows only important details and hide implementation. (Hides how sth works; shows what it does.)
Importances: 
    -Reduce complexity
    -Improves security
    -Focus on essential features
    -Cleaner system designs
Application:
    -APIs
    -Payment systems
    -Framework
    -Large application
"""

#Payment System
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")
p = CreditCard()
p.pay(10000)      
b = UPI()  
b.pay(20)

#class Vehicle with start() method, followed by car and bike implementing
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with the key!")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick!")

c = Car()
b = Bike()
c.start()
b.start()

#class Course 
from abc import ABC, abstractmethod
class Course(ABC):
    @abstractmethod
    def fees(self):
        pass
class MIT(Course):
    def fees(self):
        print("The MIT course goes for only Ksh. 50,000")
class DataScience(Course):
    def fees(self):
        print("Data Science course goes for only Ksh. 60,000")
class CyberSecurity(Course):
    def fees(self):
        print("Cyber Security course goes for only Ksh. 55,000")
class AIandML(Course):
    def fees(self):
        print("Artificial Intelligence and Machine Learning goes for only Ksh. 70,000")

m = MIT()
d = DataScience()
c = CyberSecurity()
a = AIandML()

m.fees()
d.fees()
c.fees()
a.fees()

#abstract Shape and area implemented
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 22/7 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
c = Circle(7)
r = Rectangle(10, 5)
print("Area of Circle: ",c.area())
print("Area of Rectangle: ",r.area())

