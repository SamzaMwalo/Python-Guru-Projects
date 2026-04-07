"""
OBJECT ORIENTED PROGRAMMING(OOP) - Classes And Objects
OOP - This is organising code using objects and classes
Class - This is a blueprint to create objects
Object - This is an instance of a class
"""

#class car with brand and price
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

toyota = Car("Toyota", "Ksh 1,800,000")
print(toyota.brand)
print(toyota.price)

#calculation of the area of a rectangle
class  Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

R1 = Rectangle(15, 9)
print("Area: ", R1.area())

"""
#student with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def studentResults(self):

s1 = Student("Samwel", "70")
s1.studentResults()
print("============================")
print("First student: ", self.name)
print("============================")
"""

#bank account class with deposit function
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("New Bank Balance: ", self.balance)

acc = BankAccount(1000)
acc.deposit(500)












