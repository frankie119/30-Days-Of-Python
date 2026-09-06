#Day 2: 30 Day of python programming

First_name = "Frankie"
Last_name = "O'Hara"
Full_Name = "Frankie O'Hara"
Country = "Ireland"
City = "Derry"
Age = 22
Year = 2026
is_Married = False
is_True = True
is_Light_on = False
Hair, Eyes, Ethnicity = "Brown", "Brown", "White"

print(type(Last_name))
print(type(Full_Name))
print(type(Country))
print(type(City))
print(type(Age))
print(type(Year))
print(type(is_Married))
print(type(is_True))
print(type(is_Light_on))
print(type(Hair))
print(type(Eyes))
print(type(Ethnicity))

Length1 = len(First_name)
Length2 = len(Last_name)
Length3 = (Length1 - Length2)


print("The length of my first name is", Length1)
print("The length of my last name is", Length2)
print("The difference between the length of my first name and last name is", Length3)

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_one % num_two
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

radius_input = input("What is the radius?  ")
radius = int(radius_input)
pie = 3.14

area_of_circle = pie*radius**2
# circumference = 2*pie*radius

print("The area of the circle is", int(area_of_circle))
# print("The circumference of the is", int(circumference))

user_firstName = input("What is your firstname? ")
user_lastName = input("What is your lastname? ")
user_Country = input("What country are you from? ")
user_age = input("What is your age? ")

print("First name: ", user_firstName)
print("Last name: ", user_lastName)
print("Country: ", user_Country)
print("Age: ", user_age)