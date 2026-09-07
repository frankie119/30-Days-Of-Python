#1. Declare an epty list 
empty_list = []

#2. Declare a list with more than 5 items
fruits = ["Apple", "Pear", "Bannana", "Orange", "Kiwi", "Mango", "Watermelon"]

#3.Find the length of your list
print(len(fruits))

#4. Get the first item of the list
print(fruits[0])

#4b. Get the middle item of the list
middle_item = int(len(fruits)/2)

print(fruits[middle_item])

#4c. Get the last item
last_item = int(len(fruits) - 1)
print(fruits[last_item])

#5. Declare a list called mixed_data_types, put you (name,age,height, martial status, address)
mixed_data_types = ["Frankie", 22, "6ft:1", "Not married", "1 an cluain ghlas crescent"]
#6. Declare a list variable name 'it_companies' and assign initial values Facebook, Google, Micrisoft, Apple, IBM, Oracle, Amazon
it_companies = ["Facebook", "Google", "Micrisoft", "Apple", "IBM", "Oracle", "Amazon"]

#7. Print the list using print()
print(it_companies)
print(mixed_data_types)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first item
print(it_companies[0])
#9b Print the middle company
middle_company = int(len(it_companies)/2)
print(it_companies[middle_company])
#9c Print the last company
last_company = int(len(it_companies)-1)
print(it_companies[last_company])

#10. Print the list after modifying one of the component 
print(it_companies[0])
it_companies[0] = 'Meta'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append("Anthropic")
print(it_companies)

#12. Add an it company to the middle of it companies
it_companies.insert(4, 'Sony')
print(len(it_companies)/2)
print(it_companies)

#13 Change one of the it companies names to uppercase
second_item = it_companies[1]
it_companies[1] = second_item.upper()
print(it_companies)

#14. Join the it companies with a string '#'
it_companies = '#, '.join(it_companies)
print(it_companies)

#15. Check if a certain company exists in the it_companies list
does_exist = 'Meta' in it_companies
print(does_exist)

#16. Sort the list using sort() method
it_companies = it_companies.split()
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#18. Slice out the first 3 companies from the list
first_three = it_companies[0:3]
print(first_three)

#19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

#20. Slice out the middle it company or it companies from the list
print(len(it_companies))
middle_company = it_companies[4:5]
print(middle_company)

#21. Revove the first company from the list
it_companies.pop(0)
print(it_companies)

#22. Remove the middle item from the list
middle_item = int(len(it_companies)/2)
it_companies.pop(middle_item)
print(it_companies)

#23. Remove the last item from the list
it_companies.pop()
print(it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25. Destroy the list completely
del it_companies

#26. Join the following list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

joined_list = front_end + back_end
print(joined_list)

#27. After joining the lists in question26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after redux
full_stack = joined_list.copy()
#then insert Python and SQL after redux
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#Exercises: Level 2
#The following is a list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)

print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

#Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# Find the median age
print(len(ages)/2)
median_age = ages[6]
print(median_age)

#Find the average age
average_age = sum(ages) / len(ages)
print("The average age is {:.1f}".format(average_age))

#Find the range of the ages
range = ('{} - {} = {}'.format(max_age, min_age, max_age - min_age))
print("The range is {}".format(range))

# Compare the value of (min - average) and (max-average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

print(f"The difference between min and average is: {min_diff}")
print(f"The difference between max and average is: {max_diff}")

#Find the middle country(ies) in the countries list
countries = countries = [
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

middle_country = len(countries)/2
print(middle_country)

middleCountry_1 = countries[97]
middleCountry_2 = countries[98]
print(f"The middle two countries are {middleCountry_1} and {middleCountry_2}")

#Divide the countries list into two equal lists if it is even if not one more country for the first have
country_list_1 = countries[0:98]
country_list_2 = countries[98:]

print("The first half of the countries")
print(country_list_1)

print("The second half of the countries")
print(country_list_2)

print(len(country_list_1))
print(len(country_list_2))

''' 
['China', 'Russia', 'USA', 'Finland', 'Sweeden', 'Norway', 'Denmark']
Unpack the first three countries and the rest as scandic countries,

'''

Big_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweeden', 'Norway', 'Denmark']
Ch, Ru, US, *scandic = Big_countries

print(Ch)
print(Ru)
print(US)
print(scandic)

