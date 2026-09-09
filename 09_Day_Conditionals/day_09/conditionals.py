"""1. Get user input("Enter your age"). 
    if user is 18 or older give feedback to wait 
    for the missing amount of years"""
"""
age = input("Enter your age: ")

if int(age) >= 18:
  print("You are old enough to drive")
else:
  years_to_18 = 18 - int(age)
  print(f"You need {years_to_18} more years to learn to drive")

"""

"""2. Compare the values of my_age and your_age using
      if else. Who is older (me or you)? use input("Enter your age:") to get
      the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
      'years for bigger differnces, and a custom text if my_age == your_age
"""
"""
my_age = 22
your_age = int(input("Enter your age: "))
years_between = abs(my_age - your_age)

# compare ages
if my_age == your_age:
  print("We are the same age")
elif my_age > your_age:
  if years_between == 1:
    print("I am 1 year older than you")
  else:
    print(f"I am {years_between} years older than you")
else:
  if years_between == 1:
    print("You are 1 year older than me")
  else:
    print(f"You are {years_between} years older than me")
"""
'''
Get two numbers from the user uning input prompt. If a is greater than b return a is greater than b,
if a is less than b return a is smaller than b,
 else a is equal to b
'''
"""
a = input("Enter number one")
b = input("Enter number two")

if a > b:
  print("a is greater than b")
elif a < b:
  print("a is less than b")
else:
  print("a is equal to b")
"""

# Level 2
  
"""
1. Write code which gives grade to students according to their scores
"""
"""
score = int(input("Please enter your score: "))

if score >= 90:
  print("You got an A")
elif score >= 80:
  print("You got a B")
elif score >= 70:
  print("You got a C")
elif score >= 60:
  print("You got a D")
else:
  print("You got an F, maybe more studying has to be done :(")

"""

"""
2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""
"""

month = input("Enter a month: ")

if (month == "September" or month == "October" or month == "November"):
  print("The season is Autumn")
elif (month == "December" or month == "January" or month == "Febuary"):
  print("The season is Winter")
elif (month == "March" or month == "April" or month == "May"):
  print("The season is Summer")
elif (month == "June" or month == "July" or month == "Augest"):
  print("The season is Summer")
else:
  print("You have entered an invalid month")

"""

"""
3. The following list contains some fruits:
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list 
and print the modified list. If the fruit exists print
('That fruit already exist in the list')

"""
"""
fruits = ['bannana',  'orange', 'mango', 'lemon']
fruit_input = input("Please enter a fruit: ")

if fruit_input in fruits:
  print("The fruit already exists in the list")
else:
  fruits.append(fruit_input)
  print(f"{fruit_input} has been added to the list")
  print(fruits)

"""

# level 3

"""
1. Here we have a person dictionary.
* Check if the person dictionary has skills key, 
if so print out the middle skill in the skills list.
* Check if the person dictionary has skills key, 
if so check if the person has 'Python' skill and print out 
the result.
* If a person skills has only JavaScript and React, 
print('He is a front end developer'), 
if the person skills has Node, Python, MongoDB, print
('He is a backend developer'), if the person skills has React, 
Node and MongoDB, Print('He is a fullstack developer'), 
else print('unknown title') - 
for more accurate results more conditions can be nested!
* If the person is married and if he lives in Finland, 
print the information in the following format:
"""
# dictionary
person={
  'first_name': 'Asabeneh',
  'last_name': 'Yetayeh',
  'age': 250,
  'country': 'Finland',
  'is_married': True,
  'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address': {
      'street': 'Space street',
      'zipcode': '02210'
}
}
only_JS_react = set(person['skills']) == {'JavaScript', 'React'}
has_node_python_mongodb = {'Node', 'Python', 'MongoDB'}.issubset(person['skills'])
has_react_node_mongodb = {'React', 'Node', 'MongoDB'}.issubset(person['skills'])

if ('skills' in person):
  middle_index = len(person['skills']) // 2
  middle_skill = person['skills'][middle_index]
  print(middle_skill)
  if('Python' in person['skills']):
    print(person['skills'])
  if (only_JS_react is True):
    print("He is a front end  developer")
  elif (has_node_python_mongodb):
    print("He is a backend developer")
  elif (has_react_node_mongodb):
    print("He is a fullstack developer")
  else:
    print("Unknown title")
  if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} lives in Finland. He is married")
  else:
    print("The person either does not live in Finland or they are not married")
else:
  print("No skills are listed")

  
    
