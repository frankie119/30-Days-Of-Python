# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)

# 2. Flatten the following list of lists to a one dimensional list
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

"""
3. Using list comprehension create the following list of tuples.
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

"""


multiplication = [(i, 1) + tuple(i **p for p in range(1,6)) for i in range(11)]
for row in multiplication:
  print(row)

# 4. Flatten the following list to a new list
a = ["Country", "Capital"]
countries = [[('Finland', 'Helsinki')], [('sw3den', 'stockholm')],[('Norway', 'Oslo')]]
abv = [[country.upper(), country[:3].upper(), capital.upper()]for sublist in countries for country,capital in sublist]
print(abv)

# 5. Change the following to a list of dictionaries:
country_dict = list(map(lambda sublist: {'country': sublist[0][0].upper(), 'city': sublist[0][1].upper()},countries))
print(country_dict)

# 6. Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],[('Donald', 'Trump')],[('Bill', 'Gates' )]]
concat_str = [' '.join(name) for sublist in names for name in sublist]
print(concat_str)

#7. Write a lambda function which can solve a slope or y intercept of a linear equation
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(2,3,4,10))

#Solve the y intercept
y_intercept = lambda m, x, y: y - (m* x)