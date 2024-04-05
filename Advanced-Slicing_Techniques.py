# Advanced Slicing Techniques 3 Task 1
# The aim of tis assignment is to master the are of slicing in Python lists.

# Extract the temperautres for a month, and you'd like to extract specific data
# from it.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

week_2 = temperatures[7:14]
print(week_2)

# Advanced Slicing Techniques 3 Task 2
# Extract all the temperatrues abobe 100.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

above_100 = temperatures[23:]
print(above_100)

# 2nd solution
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
above_100 = []
 
for temp in temperatures:
  if temp > 100:
    above_100.append(temp)
print(above_100)

# 
# Advanced Slicing Techniques 3 Task 3
# Reverse the list and extract temperatures from the 5th to the 10th day of the list.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temperatures.reverse()
print(temperatures)

fifth_day = temperatures[5]
print(fifth_day)
tenth_day = temperatures[10]
print(tenth_day) 

# second solution
fifth_day_negative = temperatures[-5]
print(fifth_day_negative)
tenth_day_negative = temperatures[-10]
print(tenth_day_negative)