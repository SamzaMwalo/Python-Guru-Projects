"""
STANDARD LIBRARIES IN PYTHON - Date Time Math Random
"""
# 1. DateTime Module  (Works with Date and Time)
"""
USES:
-Timestamps
-Logging
-Scheduling
-Data Analysis
-Get current date and time
"""

from datetime import datetime
now = datetime.now()
print("Current Date and Time: ", now)

from datetime import date
today = date.today()
print("Today's Date: ", today)

from datetime import datetime
formatted = datetime.now()
print("Formatted Date is: ", now.strftime("%d/%m/%y"))

# 2. Maths Module (Mathematical Functions)
"""
USES
-Scientific Calculations
-Data Analysis
-Geomerty
"""
"""
TYPES
math.ceil() - Round up
math.floor() - Round down
math.sqrt() - Square root
math.pi() - PI constant
math.exp() - exponential
math.power(x, y) - x to power of y
math.sin(), math.cos(), math.tan() - Trigonometric Functions
math.log() - Natural logarithm
math.log2() - Base-2 logarithm of x
math.asin(), math.acos(), math.atan() - Inverse Trigonometric Function
"""

import math
print("Squareroot of 36: ", math.sqrt(36))
print("Round down of 4.5 is: ", math.floor(4.5))
print("Round down of 4.5 is: ", math.ceil(4.3))
# etc


# 3. Random Module (Generate Random Values)
"""
USES
-Games
-Simulations
-OTP Generation
-Testing
-Random Number
"""

import random
colors = ["Blue","Green","Red","Grey","Black","Pink","Purple"]
print("Just a random colour: ", random.choice(colors))

import random
print("Random from a range(1-20): ", random.randint(1, 20))

import random
numbers = [1,2,3,4,5]
print("Random from a list(1-5): ", random.choice(numbers))

import random
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print("Arranged with no sequence: ", numbers)

from datetime import datetime, date
now = datetime.now()
today = date.today()
print("Its Currently: ", now, "and Today is: ", today)


# 4. Generating an OTP
import random 
otp = random.randint(100000, 999999)
print("OTP: ", otp)
