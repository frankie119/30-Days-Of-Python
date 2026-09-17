from cmath import sqrt
import math
import keyword
from countries_data import countries_data
#1. Declare a function 'add_two_numbers'. It takes two parameters and returns a sum
def add_two_numbers(num1,num2):
  sum = num1 + num2
  return sum

print("sum:",add_two_numbers(54,72))

#2. Write a function that calculate the area of a circle
def area_of_circle(r):
  pi = 3.14
  area = pi * r ** 2
  return area
print(f"The area of the circle is:", area_of_circle(10))

"""
3. Write a function called add_all_nums which takes arbitrary number of arguements and sums of all the arguements.
Check if all the list items are number types.
If not do give reasonable f3dback
"""
def add_all_nums(*args):
  total = 0
  for nums in args:
    if type(nums) == int or type(nums) == float:
     total += nums
    else:
      print(f"Unable to add character to total because {nums} is of type {type(nums)}")
      
  return total
print("Total:", add_all_nums(4,3,4,3,23))
print("Total:",add_all_nums("String","True", False, 4, 7))
print("Total:", add_all_nums(34.6, 37,2,44.9))

"""
4. Temperature in C can be coverted F using this formula F = (C*9/5) + 32
Write a function which converts C to F, convert celcius to farrenheit.
"""
def convert_to_fahrenheit(temp):
  fahrenheit = (temp * 9/5) + 32
  return f"{fahrenheit}F"
print("Temperature to Fahrenheit conversion:", convert_to_fahrenheit(28))

"""
5. Write a function called check season, it takes a month parameter and returns the season:
Autumn, Winter, Spring, Summer
"""
def check_season(month):
  if month == "June" or month == "July" or month == "Augest":
    return 'Summer'
  elif month == "September" or month == "October" or month == "November":
    return 'Autumn'
  elif month == "December" or month == "January" or month == "Febuary":
    return 'Winter'
  elif month == "March" or month == "April" or month == "May":
    return 'Spring'
  else:
    return "Invalid month"

print(check_season("December"))

"""
6. Write a function called 'calculate_slope' which return the slope of linear equation 
"""
def calculate_slope(a, b):
  slope = -a/b
  return slope
print("The slope is: {:.2f}".format(calculate_slope(2,3)))

"""
Quadratic equation is calculated as follows: ax**2 + bx + c = 0.
Write a function which calculates solution set of a quadratic equation
"""
def solve_quadratic_eqn(a,b,c):
  discrimant = (b*b) - (4 * a * c)
  sqrt_discrimant = sqrt(discrimant)
  x1 = -b + sqrt_discrimant / 2 * a
  x2 = -b - sqrt_discrimant / 2 * a
  return x1, x2

print(solve_quadratic_eqn(45, 72, 97))

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of a list
def print_list(lst):
  for i in lst:
    print(i)
fruits = ["apple", "bannana", "cherry", "strawberry", "orange"]
print_list(fruits)

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array
def reverse_list(array):
  start_index = 0
  end_index = len(array) - 1
  #swap elements
  while start_index < end_index:
    array[start_index], array[end_index] = array[end_index], array[start_index]
    start_index += 1
    end_index -= 1
  return array
array = [1,2,3,4,5]

print(reverse_list(array))
print(reverse_list(["A", "B", "C"]))

# 10. Declare a function named capitalize_list_items
def capitalize_list_items(items):
  capitalized = []
  for i in items:
     u = i.upper()
     capitalized.append(u)

  return capitalized

print(capitalize_list_items(["car", "bike", "tractor"]))

# 11. Declare a function name add_item. it takes a list and an item parameters.
#  It returns a list with the item added at the end 
def add_item(lst, item):
  lst.append(item)
  return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))

numbers = [2,3,7,9]
print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameter.
#  It returns a lsit with the item removed from it
def remove_item(lst, item):
  if item in lst:
    lst.remove(item)
  else:
    return("Invalid item")
  return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'apple'))

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))


numbers = [2,3,7,9]
print(remove_item(numbers, 3))
    
# 13. Declare a function named sum_of_numbers. It takes a number parameter
# and adds all the numbers in that range

def sum_of_numbers(n):
  total = 0
  for i in range(0, n + 1):
    total += i 
      
  return total

print(sum_of_numbers(5))
print(sum_of_numbers(20))

# 14. Declare a function name sum_of_odds. It takes a number parameter and adds
# all the odd numbers in that range
def sum_of_odds(n):
  total = 0
  for i in range(0, n+1):
    if i % 2 != 0:
      total += i

  return total

print(sum_of_odds(5))
print(sum_of_odds(10))

# 15. Declare a function name sum_of_evens. It takes a number parameter and adds
# all the even numbers in that range
def sum_of_evens(n):
  total = 0
  for i in range(0, n+1):
    if i % 2 == 0:
      total += i

  return total

print(sum_of_evens(5))
print(sum_of_evens(10))

# Exercises level 2

#1. Declare a function named even_odds. 
# It takes a positive integer as parameter and it counts number of even and odds 
# in the number

def evens_and_odds(n):
  even_count = 0
  odd_count = 0
  for i in range(0, n+1):
    if i % 2 == 0:
      even_count += 1
    elif i % 2 != 0:
      odd_count += 1
    else:
      return("Please enter a positive integer")
  return(f"The number of odds are {odd_count}\nThe number of evens are {even_count}")

print(evens_and_odds(100))

# Call your function factorial, it takes a whole number as a parameter and it return
#  a factorial of the number

def calculate_factorial(n):
  factorial = 1

  if n > 0:
    while n != 1:
      factorial *= n
      n -= 1
  
  return factorial

  

print(calculate_factorial(4))

#2. Call your function is_empty,
#  it takes a parameter and check if it is empty or not

def is_empty(s):
  if s.strip():
    return("It's not and empty or blank string")
  else:
    return("It's an empty or blank string")

print(is_empty('string'))

def calculate_mean(lst):
  mean = sum(lst)/len(lst)
  return mean

mean_lst = [4,5,4,7,5,2,8,6]
print(calculate_mean(mean_lst))

def calculate_median(lst):
  middle_value = len(lst) / 2
  median = lst[int(middle_value)]
  return median

median_lst = [4,5,6,7,8]
print(calculate_median(median_lst))

def calculate_mode(lst):
  if lst == []:
    return None
  else:
    return max(set(lst), key=lst.count)

print(calculate_mode([4,5,6,6,7,7,7,8,8,8,8]))

def calculate_range(lst):
  range = max(lst) - min(lst)
  return range

print(calculate_range([4,5,6,7,89]))

def calculate_variance(lst):
  # Calculate mean
  mean = round(sum(lst) / len(lst), 2)

  # Calculate the variance using a list comprehension
  var = round(sum((xi - mean) ** 2 for xi in lst) / len(lst), 2)
  return var

print(calculate_variance([5,6,7,8,9,6]))

# Write a function that calculates standard deviation
def stdev(xs):
  m = calculate_mean(xs)
  var = sum(abs(x-m) for x in xs) / len(xs)
  return sqrt(var)

# 4. Write a function called greet which takes a default argument, name. If no arguement is 
# supplied it should print "Hello, Guess!", otherwise it shoould
# greet the person

def greet (name = None):
  
  if name == None :
    return "Hello, Guest!"
  else:
    return f"Hello, {name}!"

print(greet("Frankie"))
print(greet())

#5. Create a function called show_args to take an arbitrary
#  number of named arguements and print their names and values

def show_args(**args):
  for k, v in args.items():
    print(f"{k}: {v}, ", end='')
  print()
  
my_dict = {"name": "Alice", "age": 22, "city": "NeyYork"}
show_args(**my_dict)

# Exerccises: level 3

# Write a function called 'is_prime', 
# which checks if a number is prime



def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

print(is_prime(4))
print(is_prime(8))

def is_unique(lst):
    seen = list()
    return not any(i in seen or seen.append(i) for i in lst)
    
print(is_unique([1,2,3,4,5,6]))
print(is_unique([1,2,23,2,3,4,32,1]))

#3 Write a function which checks if all items of the list are of the same data types
def is_same_type(lst):
 if all(map(lambda x: str(x).isdigit(), lst)):
   lst = list(map(int,lst))
   print("all are integer")
   print(lst)
   return True
 elif all(isinstance(item, str) for item in lst):
   print("all are strings")
   print(lst)
   return True
 elif any(map(lambda x: str(x), lst)):
   print("mixed dtype")
   print(lst)
   return False

x = [1,3,"two"]
y = [1,2,3]

print(is_same_type(x))
print(is_same_type(y))

# 4. Write a funtion which checks if the provided variable is a valid python variable

def is_valid (var):
  
  if not var.isidentifier() :
    return "This is an invalid python variable"
  elif keyword.iskeyword(var):
    return "This is a invalid python variable"
  else:
    return "This is an valid python variable"

print(is_valid("?$$$$&"))
print(is_valid("on"))

#5. Go to the data folder access the countries-data.py file


# Create a function that returns the 10 most spoken languages in the world

def most_spoken_languages(countries_data):
  
  frequency = {}
  for country in countries_data:
    for language in country['languages']:
      if language in frequency:
        frequency[language] += 1
      else:
        frequency[language] = 1
  top10 = sorted(frequency.items(), key = lambda kv: kv[1], reverse = True)[:10]
  print(top10)
  return top10

(most_spoken_languages(countries_data))

def most_populated_countries(countries_data):

  top_10_population = sorted(countries_data, key = lambda x: x['population'],
  reverse = True)[:10]
  f_top_10 = list[top_10_population]
  f_top_10 = [
    (country['name'], country['population']) for country in top_10_population

  ] 
  
  return f_top_10

print(most_populated_countries(countries_data))