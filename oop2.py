"""
OBJECT ORIENTED PROGRAMMING(OOP) - Encapsulation
Encapsulation - This is protecting data inside a class
Importance:
    -Data security
    -Controlled access
    -Prevent accidental changes
    -Cleaner code structure
Level Summary:
    -Public ==> name (fully accessible)
    -Protected ==> _name(internal use)
    -Private ==> __name(hidden)
"""

#Bank Account Proctection
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
    

#employee with private salary
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary

E1 = Employee(50000)
print("Salary: ", E1.get_salary())






