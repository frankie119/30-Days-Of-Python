"""1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a singfle string. 'Thirty Days Of Python'
first = 'Thirty'
second = 'Days'
third = 'Of'
fourth = 'Python'
space = ' '

concat_str = first + space + second + space + third + space + fourth
print(concat_str)
"""

"""2. Concatenate the string 'Coding', 'For', 'all'
Coding = 'Coding'
For = 'For'
All = 'All'

message = f"{Coding} {For} {All}"
print(message)
"""

#3. Declare the variable named company and assign it to an initial value 'Coding For All'
company = 'Coding For All'
sub_string = 'Coding'
print(company)
"""
print(len(company))
# convert the sentense to uppercase
print(company.upper())
# convert the sentence to lowercase
print(company.lower())
# Capitalize method 
print(company.capitalize())
# Built in Title method
print(company.title())
# Built in swapcase method
print(company.swapcase())
"""
""" Slicing 
first_word = company[0:6]
print(first_word)
print(company.index('Coding'))
print(company.rindex('Coding'))
"""
if (company.find(sub_string) != 1):
  print("True")
else:
  print("False")

replace_str = company.replace('Coding', 'Programming')
print(replace_str)

communal = 'Python For Everyone'
All = communal.replace('Everyone', 'All')
print(All)

#13. Split the string 'Coding For All' using space as the seperator (split())
print(company.split())
#Q.14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
organization = " Facebook, Google, Micrisoft, Apple, IBM, Oracle, Amazon "
print(organization.split(', '))

#15.What is the character at index 0 in the string Coding For All.
first_letter = company[0]
print(first_letter)

#16. What is the last index of the string Coding For All.
last_letter = len(company) - 1
print(last_letter)

#17 What character is at index 10 in "Coding For All" string.
print(company[10])

#18.Create an acronym or an abbreviation for the name 'Python For Everyone'.
split_word = communal.split()
acronym = split_word[0][0] + split_word[1][0] + split_word[2][0]
print(acronym)
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
word = company.split()
abv = word[0][0] + word[1][0] + word[2][0]
print(abv)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

#25.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sence = "You cannot end a sentence with because because because is a conjuction"
print(sence.index('because'))
print(sence.rindex('because'))
because = sence[31:55]
print(because)

#Q.28 Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
#Q.29 Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))

#Q.30 '   Coding For All      '  , remove the left and right trailing spaces in the given string
space_str = '   Coding For All     '
str = space_str.strip()
print(str)

#Q.31 Which one of the following variables return True when we use the method isidentifier()
one = '30DaysOfPython'
two = 'thirty_days_of_python'

print(one.isidentifier())
print(two.isidentifier())

#Q.32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

#Q.33 Use the new line escape sequence to seperate the following sentences.
multiline_str = ''' I am just enjoying this challenge.\n I just wonder what is next.'''
print(multiline_str)

#Q.34 Use a tab escape sequence to write the following lines.
template = "{:.12}{:>5} {:<10}{:>12}"
print(template.format("Name", "\tAge", "\tCountry", "\tCity\n"))
print(template.format("Asabeneh", "\t250", "\tFinland", "\tHelsinki"))

#Q.35 Use the string formatting method to display the following
radius = 10
pi = 3.14
area = pi*radius**2

formatted_str = 'The area of a circle with a radius {} is {:.2f}'.format(radius, area)
print(formatted_str)

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a,b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

