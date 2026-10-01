import re
import keyword

# Counting the most frequent word
paragraph = '''
I love teaching.
If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
'''

def top_words():
  words = re.findall(r'\w+', paragraph)
  frequency = {}
  for word in words:
    if word in frequency:
      frequency [word] += 1
    else:
      frequency [word] = 1
  top_words = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)

  for k,v in top_words:
    print(f"{k}: {v}")
  return frequency
  
top_words()

"""
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction,
0 at origin, 4 and 8 in the positive direction. 
Extract these numbers from this whole text and find the distance between the two furthest particles.
"""
text = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction,
0 at origin, 4 and 8 in the positive direction.'''

matches = re.findall(r"-?\d+", text)
points = list(matches)
print(f"points = {points}")

int_points = [int(p) for p in points]
sorted_points = sorted(int_points)
print(f"sorted points = {sorted_points}")

distance = max(sorted_points) - min(sorted_points)

print(f"distance = {max(sorted_points)} -({min(sorted_points)}) = {distance}")

def is_valid_variable(var):
  if var := re.search(r"^[a-zA-Z_]\w*$",var) and not keyword.iskeyword(var):
    return True
  else:
    return False

print(is_valid_variable("time"))
print(is_valid_variable("9time"))
print(is_valid_variable("else"))

"""
level  3:
Clean the following text. After cleaning, count three most frequent words in the string
"""

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; 
&as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple.
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(txt):
  matches = re.sub((r'%|@|&|#|;|\$|!|'), '', txt)
  return matches

print(clean_text(sentence))
cleaned_text = clean_text(sentence)

def most_frequent_words():
  words = re.findall(r'\w+', cleaned_text)
  frequency = {}
  for word in words:
    if word in frequency:
      frequency [word] += 1
    else:
      frequency [word] = 1
  frequent_words = sorted(frequency.items(), key = lambda kv: kv[1], reverse=True)[0:3]
  return frequent_words

print(most_frequent_words())