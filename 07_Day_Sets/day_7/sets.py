# sets
it_companies = {'facebook', 'Google', 'Micrisoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Find the length of the set 'it_companies'
print(len(it_companies))

#2. Add Twitter to it_companies
it_companies.add('Twitter')

#3. Insert multiple it_companies at once to the set it_companies
it_companies.update(['Anthropic', 'Instagram', 'meta'])

#4. Remove one of the IT companies from the set
it_companies.remove('facebook')

#5. What is the difference between romove and discard
# When we use remove(), amd the item is not found then it will throw and error. 
# However when we use discard() on an item that dosnt exist, we will get no error
#eg. 
# it_companies.remove('facebook')
print(KeyError)
print(it_companies.discard('facebook'))

# level 2
#1. Join A and B
C = A.union(B)
D = B.union(A)

# Print the combined set
print(C)

#2. Find A intersection B
print(A.intersection(B))

#3. Is A subset of B
print(A.issubset(B))

#4. Is subset A and B disjoint sets
print(A.isdisjoint(B))

#5. Join A with B and B with A
# Join A with
print(A.union(B))
print(B.union(A))


#6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7. Delete the sets completely
del A
del B
del C
del D

# Level 3
#1 Convert the ages to a set and compare the length of the list and the , which one is bigger
age_st = set(age)
difference_between = len(age) - len(age_st)
if len(age) > len(age_st):
  print(f"The list is bigger by {difference_between} items")
else:
  print(f"The set is bigger by {difference_between} items")


#2. Explain the difference between the following data types: string, list, tuple, set
# A string is a sequence of characters used to represent text. In Python, strings are immutable
# A list is an ordered, mutable collection. It can hold any data type (not just strings/ints), allows duplicates, amd items can be updated. Created with '[]'
# A tuple is an ordered, immutable collection. The items cannot be updated or changed after creation. Created with '()'.
# A set is an unordered collection of unique items. Becasue it is unindexed, you cannot update specefic items, but you can add or reveiw items. Created '{}'

#3. How many unique words have been used in the sentence
sentence = ("I am a teacher and I love to inspire and teach people")

# Split the string and assign it to a variable
words = sentence.split()

print(sentence)

# Covert the split list to a set
sent_st = set(words)

# Print the set
print(sent_st)

# Get the length of the set
len_uniqueWords = len(sent_st)

print(f"There are {len_uniqueWords} unique words in the sentence.")