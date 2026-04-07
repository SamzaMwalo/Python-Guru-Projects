#BANK ACCOUNT SYSTEM

#Abstract Base Class

from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, name, balance):
        self.name =  name
        self.__balance = balance    #encapsulated

    @abstractmethod
    def account_type(self):
        pass
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("You have deposited: ", amount)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("You have withdrawn: ", amount)
        else:
            print("You've got insufficient balance!!")
    def get_balance(self):
        return self.__balance
    

# Saving Account
class NewSavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"
    

#Existing Account
class ExistingAccount(BankAccount):
    def account_type(self):
        return "Exisiting Account"
    

#Test the System
First_Account = NewSavingsAccount("Samwel", 10500)
print(First_Account.account_type())
First_Account.deposit(10150)
First_Account.withdraw(900)
print("Your balance is: ", First_Account.get_balance())

Second_Account = ExistingAccount("Benjamin", 16000)
print(Second_Account.account_type())
Second_Account.deposit(20050)
Second_Account.withdraw(1300)
print("Your balance is: ", Second_Account.get_balance())


