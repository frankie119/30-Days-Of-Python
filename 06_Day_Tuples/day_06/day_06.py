#1. Create an empty tupe
empty_tuple = ()

#2. Create a tuple containing names of your sisters and your brothers 
sisters = ("Emily", "Grace")
no_sisters = len(sisters)

brothers = ("Tony", "Bob")
no_brothers = len(brothers)

parents = ("Margaret", "John")

#3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

#4. How many siblings do you have?
no_siblings = len(siblings)

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + parents
no_family_members = len(family_members)
print(family_members)

# Exercise: level 2
#1. Unpack siblings and parents from family_members
sibling1, sibling2, sibling3, sibling4, mother, father = family_members
print(mother)
print(father)
print(sibling1)
print(sibling2)
print(sibling3)
print(sibling4)

# Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp

fruits = ("Apple", "Pear", "Grape", "Orange", "Mango", "Strawberry")
vegetables = ("Carror", "Brocolli", "Parsnips", "Cabbage")
animal_products = ("Beef", "pork", "lamb", "chicken", "turkey", "duck",)

food_stuff_tp = fruits + vegetables + animal_products
# Change the about food_stuff_tp tuple to a food_stuff_lt
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp 
# first get the item that is in the middle
print(len(food_stuff_lt) / 2)
middle_item = food_stuff_lt[7:9]
print(middle_item)

# Slice out the first three items of the list
first_three_items = food_stuff_lt[0:3]
# slice out the last three items of the list
last_three_items = food_stuff_lt[-3:]

print(first_three_items)
print(last_three_items)

# Delete the food_stuff_tp completely
del(food_stuff_tp)


#Check if an item exits in a tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweeden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)