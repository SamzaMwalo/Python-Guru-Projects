"""
OBJECT ORIENTED PROGRAMMING(OOP) - Inheritance
Inheritance - This is the functionality where one class uses properties of another class
Importance:
    -Code reuse
    -Better structure
    -Easy maintainance
    -Real-world modeling
"""



#Method over-riding  -  Changes behaviour
class Animal: #Parent Class(Base class)
    def sound(self):
        print("Animal makes sound")

class Dog(Animal): #Child Class(Derived Class) - over-rides parent
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()



class Animal:
    def sound(self):
        print("Animal makes sound but ...")

class Dog(Animal):
    def sound(self):
        super().sound() #super calls Parent constructor method by:  -Reusing parent logic -Extend functionality
        print("Dog barks")

d = Dog()
d.sound()



class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def eat(self):
        print("Dog eats bones")

d = Dog()
d.eat()



class Animal:
    def eat(self):
        print("Animal eats but...")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("Dog eats bones")

d = Dog()
d.eat()

"""
Types of inheritance
    -Single Inheritance eg Animal=>Dog
    -Multiple Inheritance eg Father + Mother => Child
"""

#Employee System

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Employee: ", self.name)
class Manager(Employee):
    def manage(self):
        print("Manages team")
        
m = Manager("Mwangi")
m.show()
m.manage()

class Person:
    def __init__(self, name):
        self.name = name
    def study(self):
        print("Stud_Name: ", self.name)
class Student(Person):
    def Student(self):
        print("Goes to school to study")

s1 = Student("Samwel")
s1.study()
s1.Student()




