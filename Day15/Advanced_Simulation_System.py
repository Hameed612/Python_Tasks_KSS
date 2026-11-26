# 10. Advanced Simulation System

# Scenario:
# Simulate exam results and generate reports.

# Task:
# ● Generate random marks using random
# ● Store in NumPy array
# ● Convert to Pandas DataFrame
# ● Use OOP to represent Student
# ● Use conditions + loops to assign grades
# ● Save report to file
# ● Handle errors using try-except
# ● Use math module for statistics


# Advanced Simulation System

import random
import numpy as np
import pandas as pd
import math

# Create Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Assign grade
    def grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 50:
            return "C"

        else:
            return "Fail"


try:

    # Student names
    names = ["Rahul", "Anita", "Ravi", "Priya", "John"]

    # Generate random marks
    marks = np.array([
        random.randint(30, 100) for i in range(5)
    ])

    # Create DataFrame
    data = pd.DataFrame({
        "Name": names,
        "Marks": marks
    })

    print("Exam Results:")
    print(data)

    # Create student objects
    students = []

    for i in range(len(names)):

        student = Student(names[i], int(marks[i]))

        students.append(student)

    # Calculate average using math
    average = math.floor(np.mean(marks))

    print("\nStudent Grades:")

    # Save report into file
    with open("exam_report.txt", "w") as file:

        file.write("EXAM REPORT\n")
        file.write("----------------\n")

        for student in students:

            grade = student.grade()

            print(student.name, student.marks, grade)

            file.write(
                student.name + " " +
                str(student.marks) + " " +
                grade + "\n"
            )

        file.write("\nAverage Marks: " + str(average))

    print("\nAverage Marks:", average)
    print("Report saved successfully!")

except (ValueError, IOError) as e:

    print("Error:", e)
