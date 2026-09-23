from random import random
from random import shuffle
from random import randint
from random import choices
import string
import array

# 1. Write a function which writes a 6 digit/character random user id
def random_user_id():
  ch = (string.ascii_letters + string.digits)
  user_id = "".join(choices(ch, k = 6))
  return user_id
  
print(random_user_id())

"""
2. Modify the previous task. Declare a function named user_id_gen_user. It dosnt take any parameters but it takes
two inputs using input(). One of the inputs is the number of characters and the second input is the number of ID'S
which are supposed to be generated
"""
"""
def user_id_gen_by_user():
  no_characters = int(input("Please enter the number of characters you want: "))
  no_id = int(input("Please enter number of Ids you want: "))
  user_id_lst =  []
  
  for u in range(no_id):
    ch = (string.ascii_letters + string.digits)
    u = "".join(choices(ch, k = no_characters )) 

    user_id_lst.append(u)

  return("\n".join( user_id_lst))
  
    

print(user_id_gen_by_user())
"""

 # 3. Write a function named rgb_colour_gen. It will generate rgb colours
def rgb_color_gen():
  
  rgb_lst = []
  for i in range(3):
    rgb =(randint(0, 255))
    rgb_lst.append(rgb)
    i += 1
  rgb_tp = tuple(rgb_lst)
  return f"rgb{rgb_tp}"



print(rgb_color_gen())


# Exercise level 2
"""
1. Write a function list_of_hexa_colours which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system
is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples
"""

def hex_colours(num=None):
  if num is None:
    num = int(input("What is the number: "))

  hex_lst = []
  hexadecimal = ["a", "b", "c", "d","e","f","1","2","3","4","5","6","7","8","9"]
  hashtag = "#"

  for i in range(num):
    colour = ("".join(choices(hexadecimal, k = 6)))
    hex_colour = hashtag + colour
    hex_lst.append(hex_colour)

  return hex_lst

print(hex_colours())

"""
2. Write a function list_of_rgb which returns any number of RGB coulour in an array

"""

def list_of_rgb(num = None):
  if num is None:
    num = int(input("List the number of RGB colours you want: "))
  rgb_list = []
  for _ in range(num):
    rgb = rgb_color_gen()
    rgb_list.append(rgb)
  
  return rgb_list

print(list_of_rgb())

#3. Write a function generate_colours which can generate any number of hexa or rgb colours

def generate_colours(choice, n):
  choice = 'hexa' or 'rbg'
  if choice == 'hexa':
    return hex_colours(n)
  elif choice == 'rgb':
    return list_of_rgb(n)
  else:
    return "You have entered an invalid choice"

print(f"rgb/hexa {generate_colours('hexa', 7)}")

# Exercises level 3
# Call your function 'shuffle_list', it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):

  shuffled_list = lst.copy()
  shuffle(shuffled_list)
  return shuffled_list

print(shuffle_list(['Apple', 'Bannana', 'Orange', 'Mango', 'Pear', 'Strawberry']))

"""
Write a function which returns an array of seven random numbers in a range of 0-9.
All the numbers must be unique
"""
def random_numbers():
  num = [] 
  while len(num) < 7:
    n = randint(0,9)
    if n not in num:
      num.append(n)
    else:
      continue
  return num

print(random_numbers())