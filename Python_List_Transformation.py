# Python List Transformation 1 Task 1
# The aimm of this is to practice advanced list operatins and transformatons.
# You've been given a list of numeriacal gread froma class exam. You need to
# process and analyze these grades.

grades = [ 85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order, and display sorted  list.
grades.sort()
print(grades)

grades.reverse()
print(grades)

grades.sort(reverse=True)
print(grades)

# Pyhton List Transformation 1 Task 2
# Calcaulate the average grade and display it.

grades = [ 85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades_avg = [ (85 + 90 + 78 + 88 + 76 + 95 + 89 + 80 + 72 + 93) / 10]
print(grades_avg)

# Python List Transformaton 1 Task 3
# Replace any grade below 80 with the value failed

grades = [ 85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

for i in range(len(grades)):
  if grades[i] < 80:
    grades[i] = ("failed")
    print(grades)
    print(grades[i])
#used w3 schools loop through the index numbers
#loop runs three times? assuming is it keeps running till t finds all of values < 80




