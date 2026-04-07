"""
FUNCTIONS: A block of of reusable code that runs only when you callit and solves one specific task.
Importances:
    -Avoids unnecessary redundancy
    -Improves readability
    -Easier debugging
"""


#basic function
def greet(name):
   print("Hello")
greet('')

#functions with parameters
def greet(name):
    print("Hello", name)
greet("Samwel")

"""
Parameters: receive data
Arguments: send data
"""

#functions with return value
    #Addition
def add(a, b):
    return a + b
results = add(20, 30)
print(results)

    #Multiplication
def multiply(c, d):
    return c * d
results = multiply(10, 10)
print(results)

    #Subtraction
def minus(a, b):
    return a - b
results = minus(50, 10)
print(results)


    #Divide
def divide(x, y):
    return x / y
results = divide(30, 10)
answer = divide(100, 5)
print(answer)
print(results)


#multiple return paths... Research on this ***
def check_pass(marks):
    if marks >= 40:
        return "Pass"
    return "Fail"
results = check_pass(-1)
input(
    "Input Marks: " 
)
print(results)


#Default parameters eg: in this case, its used to return the results of a number raised to a given number
def power(base, exp=2):
    return base ** exp
print(power(3))
print(power(2, 4))

#function calling function
def square(n):
    return n * n
def cube(n):
    return square(n) * n
print(cube(5))
print(square(5))

#function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
print("Simple Interest: ", simple_interest(10000, 2.5, 10))

#function to find maximum of two
def find_max(a, b):
    if a > b:
        return a
    return b
print(find_max(40, 55))

#checking prime number
def prime_no(n):
    if n <= 1:
        return False
    for y in range(2, int(n **0.5) + 1):
        if n % y == 0:
            return False
        return True

print(prime_no(5))






