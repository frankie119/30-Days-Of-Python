#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Boots', 'color': 'Brown', 'breed': 'King Charles', 'legs': 4, 'age': 12 }
# Print the disctionary
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age,
# martial status, skills, country, address
student = {'first_name': 'Jim', 
           'last_name': 'Halpert', 
           'gender': 'male', 
           'age': '30', 
           'martial_status': "Is married", 
           "Skills": ["JS", "React", "Node", "MongoDB", "Python"], 
           'country': 'Ireland', 'city': 'Belfast', 
           'address': '1 Main Street'}

print(student)
#4. Get the length of the student dictionary
len_student_dict = len(student)
print(f"The length of the Student dictionary is {len_student_dict}")

#5. Get the value of skills and check the data type. It should be list
skills = student['Skills']
# Get the data type of the values
print(type(skills))

#6. Modify the skills values by adding on or two skills
student['Skills'].append('Html')
student['Skills'].append('Testing')
print(student)

#7. Get the dictionary keys as a list
keys = student.keys()
print(f"Dictionary Keys: {keys}")

#8. Get the dictionary values as a list
values = student.values()
print(f"Dictionary values: {values}")

#9 Change the dictionary to a list of tuples using items() method
print(student.items())

#10. Remove one of the items from the dictionary
print(student.pop('city'))

#11. Delete one of the dictionaries 
del dog