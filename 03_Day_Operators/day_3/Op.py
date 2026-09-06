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


