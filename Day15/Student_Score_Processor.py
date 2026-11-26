# 1. Student Score Processor

# Scenario:
# A teacher stores student names and marks in a list of tuples.

# Task:
# ● Convert data into a dictionary
# ● Use a loop + condition to find students scoring above 50
# ● Use math module to calculate average
# ● Store results in a text file


# Student Score Processor

import math

# Store student names and marks in tuples
students = [("pruvdi kalyan", 80), ("Annu", 45), ("Hemanth", 70), ("Hameed", 90)]

# Convert list of tuples into dictionary
student_dict = dict(students)

print("Student Details:", student_dict)

# Calculate total marks
total = 0

# Find students scoring above 50
print("\nStudents scoring above 50:")

for name, marks in student_dict.items():
    total = total + marks

    if marks > 50:
        print(name, marks)

# Calculate average using math module
average = math.floor(total / len(student_dict))

print("\nAverage Marks:", average)

# Store results in text file
with open("students.txt", "w") as file:
    file.write("Student Results\n")

    for name, marks in student_dict.items():
        file.write(name + " : " + str(marks) + "\n")

    file.write("Average Marks: " + str(average))

print("\nData saved successfully!")
