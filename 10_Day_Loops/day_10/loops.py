from countries_data import countries_data

#1. Iterate 0 - 10 using for loop, do the same using while loop
"""
for number in range(11):
  print(number)

# While Loop
count = 0
while count < 11:
  print(count)
  count += 1
"""

#2. Iterate 10-0 using for loop, do the same using while loop
"""
for number in range(10, -1, -1):
  print(number)

# While loop
count = 10
while count > -1:
  print(count)
  count -= 1

"""

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle
"""
for n in  range(1,8):
  print(n * '#')
"""
"""
4. Use nested loops to create the following
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
"""
for x in range(8):
  for y in range(1, 9):
    print('#', end=" ")
  print()
"""
"""
5. Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
"""
for n in range(11):
    print('{} * {} = {}'.format(n, n, n * n),)
"""

#6. Iterate through the list, [python, 'Numpy', 'Pandas', 'Django', 'Flask']
"""
lst = ['python', 'Numpy', 'pandas', 'django', 'flask']
for i in lst:
   print(i)
"""
#7. Use for loop to iterate from 0 to 100 and print only even numbers
"""
for n in range(0, 101):
   if n % 2 == 0:
      print(n)
"""
#8. Use for loop to iterate through 0 to 100 and print only the odd numbers
"""
for n in range(0,101):
   if n % 2 != 0:
      print(n)
"""    
# level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
running_total = 0

for n in range (101):
   running_total += n
print(f"The sum of all numbers is {running_total}")

"""
# 2. Use for loop to iterate from 0 to 100 and
print the sum of all evens and the sum of all odds

"""
even = 0
odd = 0

for n in range (0, 101):
   if n % 2 == 0:
      even += n
   else:
      odd += n
print(f"The sum of all evens is {even}. And the sum of all odds is {odd}")
   
# level 3
#1. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
"""
no_of_countries = 0
countries_with_land = []
for country in countries:
   if 'land' in country:
      countries_with_land.append(country)
print(countries_with_land)
"""


# Fruit list
"""
2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon']
 reverse the order using loop.
"""
fruits = ['bannana', 'orange', 'mango', 'lemon']
reversed_lst = []
for fruit in fruits:
   reversed_lst = [fruit] + reversed_lst
print(reversed_lst)

"""
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
"""
languages = []
no_of_languages = 0
top_languages = []
count = 0
for country in countries_data:
   for language in country["languages"]:
      languages.append(language)
unique_languages = set(languages)
no_of_languages = len(unique_languages)
print(f"The number of languages in the dictionary is {no_of_languages}")
# Time complexity for this algorithm is Big O(n)  

# Find the 10 most spoken languages in the data

frequency = {}
frequency_count = 0
for country in countries_data:
   for language in country['languages']:
      if language in frequency:
         frequency[language] += 1
      else:
         frequency[language] = 1
      top10 = sorted(frequency.items(), key = lambda kv: kv[1], reverse = True)[:10]
print(top10)

# Find the 10 most populated countries in the world
def getPopulation(countries_data):
   return countries_data['population']

top_10_population = sorted(countries_data, key = getPopulation,
reverse = True)[:10]
print(top_10_population)
for country in top_10_population:
   print(f"{country['name']}: {country['population']}")
   
      

      
      
