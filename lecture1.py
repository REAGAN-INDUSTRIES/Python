#PYTHON SYNTAX
print("500 days run")
print("Fast Track challenge")

day1_distance = 5.74
day2_distance = 5.73

total_distance = day1_distance + day2_distance
print(total_distance)

#Python ignores any number of white spaces during execution

day1_distance = 5.74
day2_distance = 5.73
day3_distance = 5.79

total_distance= day1_distance + day2_distance 
+ day3_distance
print(total_distance)   #wouldn't add day3 dist

total_distance= day1_distance + day2_distance  \
+ day3_distance
print(total_distance)    # adds the day3 distance coz of the back slash

#INDENTATION IS KEY IN PYTHON

challenge_days = 500

if challenge_days == 508:
 print(challenge_days)


#VARIABLES

day1_date = "19-Nov-2023"
day1_start_time = "6:34:00 AM"
day1_end_time = "6:55:00 AM"
day1_distance = 5.74 # in kilometers
day1_avg_pace = "03.40" # min:sec per km
day1_timer = "20:51" #min:sec

print(day1_date)
print(day1_start_time)
print(day1_end_time)

# All letters are sperated by underscores, and all are in small letters, and cannot begin with a number  (snake naming case)

#YOU can assign the variables on the same line

day1_distance, day2_distance, day3_distance = 5.74, 5.73, 5.79 
print(day1_distance, day2_distance, day3_distance)

#if you assign three variable names with less or more values, when invoked by the print statement, you get an error for either cases

#you can also delete valiables using the del keyword 
#Eg
del day3_distance
print(day3_distance) 

#Split the string to get minutes and seconds
avg_pace_day1 = "03:40"
minutes, seconds =avg_pace_day1.split(':')
print(minutes)
print(seconds)
 #You can actually print their types as well 
print(type(minutes))
print(type(seconds))
