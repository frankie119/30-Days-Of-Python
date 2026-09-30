from datetime import *



"""

Get the current day, month, year, hour, minute and timestamp from date time module

"""

# Get the current day

now = datetime.now()
day = now.day

# Get the current month
month = now.month

# Get the current year
year = now.year

# Get the current hour
hour = now.hour

# Get the minute
minute = now.minute

# Get the timetamp
timestamp = now.timestamp()

print(day, month, year, hour, minute)
print(timestamp)

# Format the current date using this format
time_one = now.strftime("%m/%d/%y, %H:%M:%S")
print(time_one)

# Today is 5 December, 2019
exercise_time = date(year=2019, month=12, day=5)
print(exercise_time)

# Calculate the difference between now and new year
today = date(year=2026,month=9,day=30)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today

print('Time left for new year: ', time_left_for_newyear)

time_difference_time = date(year=1970, month=1, day=1)
time_difference = today - time_difference_time
print(time_difference)