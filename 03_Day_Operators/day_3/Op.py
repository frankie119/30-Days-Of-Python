import math
""" 
age = 22
height = 6.00
complex_number = 1 + 1j
"""
x1,y1 = 2, 2
x2,y2 = 6,10
slope_9 = (y2 - y1) / (x2 - x1)
dx = x2 - x1
dy = y2 - y1
distance = math.sqrt((dx * dx) + (dy * dy) )
slope_8 = 2

"""
base = input("Enter the base of the triangle" )
height = input("Enter the height of the triangle" )

area = 0.5*int(base)*int(height) 
"""
""" Question 5
print("The area of the triangle is", int(area))

a = input("Enter side a:" )
b = input("Enter side b:" )
c = input("Enter side c:" )

perimeter = int(a) + int(b) + int(c)

print("The perimeter of the triangle is ", perimeter)

"""
""" Question 6 
length = input("What is the length of the rectangle")
width = input("What is the width of the rectangle")

area = int(length)*int(width)
print("The area of the rectangle is ", area)

perimeter = 2* (int(length) + int(width))
print ("The perimeter of the ractangle is ", perimeter)

"""
""" Question 7
radius = input("What is the radius of the circle")
pi = 3.14

area = pi * (int(radius)**2)
c = 2*pi*int(radius)
result = round(c, 2)

print("The area of the circle is ", area)
print("The circumference of the circle is ", result)

"""
""" Question 8
m = 2 # coefficient of x(the slope)
b = -2 # constant term (the y-intercept)
slope = m
y_intercept = b
x_intercept = -b / m

print (f"slope = {slope}")
print (f"y-intercept =  {y_intercept} + at point ({y_intercept})")
print (f"x-intercept = {x_intercept} at point ({x_intercept})")
"""

""" Question 10 - Compare the slopes of task 8 and 9 
rounded_distance = round(distance, 2)
print(f"Slope = {slope_9}")
print(f"Distance = {rounded_distance}")
print(f"The slope in Q.8 is {slope_8}")

if (slope_8 == slope_9):
  print("The slopes are equal")
elif (slope_8 > slope_9):
  print("The slope in Q. 8 is greater than the slope in Q.9 ")
else:
  print("Q. 9 has the greater slope")

"""
""" Question 11. Find the length of both 'Python' and 'Dragon'. And make a falsy statement
x = -3
y = x**2 + 6*x + 9


print(f"The value of y is {y}")

"""
"""Question 12, 13, 14, 15, 16
length_Of_Python = len("python")
length_Of_Dragon = len("dragon")

print(length_Of_Python != length_Of_Dragon)

if ("on" in "python" and "on" in "dragon"):
  print ("On is in both")
else:
  print("It is not in both")

sentence = "I hope this course is not full of jargon"
if ("jargon" in sentence):
  print(f"Jargon is included in: {sentence}")
else:
  print(f"Jargon is not included in: {sentence}")

if('on' not in "python" and "on" not in "dragon"):
  print("There is not 'on' in both dragon and python")
else:
  print("There is 'on' in both dragon and python")

float_Python = float(length_Of_Python)
print(float_Python)
str_Python = str(length_Of_Python)
print(str_Python)

number = input("Enter a number: ")
if (float(number) % 2 == 0):
  print(f"{number} is even")
else:
  print(f"{number} is odd")
"""
""" Question 17, 18, 19, 20
value = 2.7
int_value = int(value)

if (7//3 == int_value):
  print(f"It is equal to {int_value}")
else:
  print(f"It is not equal to {int_value}")

type_int = type('10')
type_str = type(10)

if (type_int == type_str):
  print("True")
else:
  print(f"'10' is a {type_int} value and 10 is {type_str} value")

try:
  if (int('9.8') == 10):
    print("'9.8' is equal to '10")
  else:
    print("'9.8' is not equal to 10")
except ValueError:
  print("int('9.8') raises a valueError - you can't direct convert a decimal string to an int")

"""
""" Question 21
hours = input("Enter hours: ")
rate_per_hour = input("Enter rate per hour: ")
weekly_earning = float(rate_per_hour) * float(hours)

print(f"Your weekly earning is {weekly_earning}")

"""
""" Question 22
no_Of_Years = input("Enter number of years you have lived: ")
seconds_lived = 60 * 60 * 24 * 365 * int(no_Of_Years)

print(f"You have lived for {seconds_lived} seconds")

"""
""" Two ways of doing Q.23
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)

for n in range (1, 6):
  print(n, n**0, n**1, n**2, n**3)
"""

