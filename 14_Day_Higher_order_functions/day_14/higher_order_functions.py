from functools import reduce
from countries import countries
from countries_data import countries_data

#1 Explain the difference betw3n map, filter and reduce
"""
map takes 2 parameter, a function and a iterable. It takes the items in the iterable and applys the fuction to each of them. Whereas the filter
function also takes to parameters, the function and the iterable.The filter function returns boolean for each item in the iterable.
It filters for each item that satifies the filtering criteria. Like the map and filter function, the reduce function takes two parameters
but it does not return another iterable, instead it returns a single value.
"""

#2 Explain the difference betw3n higher order functions, closure and decorators 
"""
Closure is when a nested function is allowed to access the outer scope of the enclosing function and returns the inner function. Whereas a decorator 
is a design pattern that allows a user to add new functionality to an existing object without modifying  its structure. Decorators are usually called 
before the defination of a function you want to decorate. And higher order function is a function that takes a function as an arguement OR returns a 
function.
"""

#3. Define a call function before map, filter or reduce
countries_lst = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(x):
  return x ** x

numbers_squared = map(square, numbers)
print(list(numbers_squared))

# filter Function
def is_long(name):
  if len(name) > 7:
    return True
  return False

long_names = list(filter(is_long, names))
print(long_names)

# Reduce function
def add_two_nums(x,y):
  return x + y

total = reduce(add_two_nums, numbers)
print(total)
# 4. Use for to print each country in the countries_lst list

print("Countries")
for country in countries_lst:
  print(country)

# 5. Use for to print each name in the names list.
print("names")
for name in names:
  print(name)

# 6. Use for to print each number in the numbers list.
print("numbers")
for number in numbers:
  print(number)

# Exercise level 2
# 1. Use map to create a new list by changing each country to uppercase in the countries_lst list

def uppCaseCountry(country):
  return country.upper()

UPCC = map(uppCaseCountry,countries_lst)
print(list(UPCC)) 

# 2. Use map to create a new list by changing each number to its square in the numbers list
squared_number = map(lambda x: x**2, numbers)
print(list(squared_number))

# 3. Use map to change each name to uppercase in the names list
Uppercase_name = map(lambda n: n.upper(), names)
print(list(Uppercase_name))

# 4. Use filter to filter out countries_lst containg 'land'
def countries_containing_land(country):
  if 'land' in country:
    return True
  return False

land_countries = filter(countries_containing_land, countries_lst)
print(list(land_countries))

# 5. Use filter to filter out countries_lst having exactly six characters

filter_countries = filter(lambda c: True if len(c) == 6 else False, countries_lst)
print(list(filter_countries))

# 6. Use filter to filter out countries_lst containg 6 letters or more 
long_countries = filter(lambda c: True if len(c) >= 6 else False, countries_lst)
print(list(long_countries))

#7. Use filter to filter out countries_lst that start with an e
def countries_beginning_with_E(country):
  if (country[0] == 'E'):
    return True
  return False

E_Countries = filter(countries_beginning_with_E, countries_lst)
print(list(E_Countries))

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
"""
"From the countries_lst list, filter out countries_lst that have fewer than 7 letters, 
convert the remaining country names to uppercase, and then concatenate them all
 together into a single sentence or string."
"""
small_countries = filter(lambda c: True if len(c)<7 else False, countries_lst)
uppercase_small_countries = map(lambda sc: sc.upper(), small_countries)
uppercase_list = list(uppercase_small_countries)

concat_str = " ".join(uppercase_list)
print(concat_str)

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_items(lst):
    only_strings = list(filter(lambda item: True if type(item) == str else False, lst))
    return only_strings

print(get_string_items(["apple", 5, "bannana", True, "Cherry", 3.14]))

#10. Use sum to sum all the numbers in the number list
def total_numbers(x, y):
  return x + y

print(reduce(total_numbers, numbers))

"""
11. Use reduce to concatenate all the countries_lst and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland
are north European countries_lst
"""
concat_c = reduce(lambda x,y: x + ("," if x else "") + y, countries_lst)


print(f"{concat_c} are north European countries_lst")

"""
Declare a function called categorize_countries that returns a list of countries_lst with some common pattern
(you can find the countries_lst list in this repository as countries_lst.js(eg 'land', 'ia', 'island', 'stan')).
"""

def categorise_countries(country):
  return 'land' in country
   
land_countries = list(filter(categorise_countries, countries))
print(land_countries)

"""
Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of 
country names starting with that letter.
"""
def No_of_letters(acc, country):
  letter = country[0]
  acc[letter] = acc.get(letter, 0) + 1
  return acc

result = reduce(No_of_letters, countries, {})

print(result)

"""
Declare a first 10 countries function - it returns a list of first 10 countries from the countries

"""
def first_10_countries():
  return countries[:10]


print(first_10_countries())

"""
Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
"""

def last_10_countries():
  return countries[-10:]


print(list(last_10_countries()))

"""
Sort countries by name, by capital, by population
"""
# Sort by name

top_names = (sorted(countries_data, key = lambda country: country["name"]))
for country in top_names:
  print(f"{country['name']}")

# Sort by capital
top_capital = (sorted(countries_data, key = lambda country: country["capital"]))
for country in top_capital:
  print(f"{country['name']}: {country['capital']}")

# Sort by population
top_population = (sorted(countries_data, key = lambda country: country["population"] ))
for country in top_population:
  print(f"{country['name']}: {country['population']}")

# Sort the ten most spoken languages by region
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

# Sort the 10 most populated countries
top_10_countries = sorted(countries_data, key = lambda country: country['population'],reverse=True)[:10]
for country in top_10_countries:
  print(f"{country['name']}: {country['population']}")