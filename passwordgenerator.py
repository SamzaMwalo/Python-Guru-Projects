""""
This is a tool that develops strong random password using letters, numbers and symbols, with user-defined length
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter password length: "))
password = generate_password(length)
print("Generate Password:", password)
