# Advanced List Methods and Identity Operators 2 Task 1
# The aim of this assignment is to delve deeper into list methods and understand the 
# nuances of idetity operators.
# You have two lists of students names. One list contains the names of students who have
# submitted their assignments, and the other list contains the names who attended the last
# class.

# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

combined_list = []

for student in submitted:
  if student in attended:
    combined_list.append(student)
print(combined_list)
print(f"The students who both submitted their assignments and attended their last class, {combined_list}")

# Advanced List Methods and Indetity Operators 2 Task 2
# Check if the two list are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if submitted == attended:
  print("It seems both lists are identical.")
else:
  print("It seems that the lists aren't identical.")
 
 
# Advanced List Methods and Indetity Operators 2 Task 3
# Using list methods, remove any student from the attended list who did not submit
# their assignment.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for student in attended:
  if student not in submitted:
    attended.remove(student)
    print(f"Removed {student} from the attended list.")
print(attended)





