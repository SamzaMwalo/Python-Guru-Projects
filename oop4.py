"""
OBJECT ORIENTED PROGRAMMING(OOP) - Polymorphism
Polymorphism - This is the use of same method name but different behaviour.
    -Poly -> many
    -Morphism -> forms
Significance:
    -Flexible code
    -Easy to extend
    -Cleaner design
    -Less conditional statements
Types:
    1. Method overriding Child class changes parent method
    2.Duck Typing (Python Styles) "eg If it walks like a duck and quacks like a duck, its a duck." Python checks behaviour and not the type
"""

#Bird class with eagle and penguin overriding fly()

class Bird:
    def fly(self):
        print("Bird flies")

class Eagle(Bird):
    def fly(self):
        print("An Eagle Flies")

class Penguin(Bird):
    def fly(self):
        print("A Penguin Never Flies")

birds = [Eagle(), Penguin()]
for b in birds:
    b.fly()



class Domestic:
    def sound(self):
        print("Animal Makes Unique Sound.")

class Dog(Domestic):
    def sound(self):
        print("A Dog Barks.")

class Cat(Domestic):
    def sound(self):
        print("A Cat Meaus.")

domestics = [Dog(), Cat()]
for d in domestics:
    d.sound()



#Payment System
class DebitCard:
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")

class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

def process_payment(method, amount):
    method.pay(amount)

process_payment(DebitCard(), 1000)
process_payment(UPI(), 500)



#Area of rectangle and circle
class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

shapes = [Circle(4), Rectangle(6, 4)]
for s in shapes:
    print("Area: ", s.area())



#Employee payment method with different types
class Employee:
    def pay(self):
        print("Employee gets salary")

class FullTime(Employee):
    def pay(self):
        print("Monthly salary paid")

class PartTime(Employee):
    def pay(self):
        print("Hourly payment made")

class Online(Employee):
    def pay(self):
        print("Paid through commissions")

employees = [FullTime(), PartTime(), Online()]
for e in employees:
    e.pay()



