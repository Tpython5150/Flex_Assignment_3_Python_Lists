# Deep Dive into Pthon Lists 4 Tasks 1, 2, 3
# The aim of tis assignment is to itegreate various list operations and methods to solve
# a complex problem

# You're organizing a school event, amd you have lists containning student names, their
# grades, and the actvities they're interrested in. 

# Filter out students who have grades below 80. Print the name, grade activity. 
# Expected Outcome; "Jane", 78, "Art".

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

students_approved = []
for i in range(len(students)):
  if grades[i] < 80: 
    print(students[i], grades[i], activities[i])
  else:
    students_approved.append(students[i])
print(students_approved)
    
# Deep Dive into Python Lists 4 Task 2 
# For the remaing students, add students name in a new list names students_approved.
# Previous 

#students_approved = []
#for x in range(len(students)):
 # if grades[x] > 80:
   # print(students[x])
   # students_approved.append(students[x])
  
#print(students_approved)