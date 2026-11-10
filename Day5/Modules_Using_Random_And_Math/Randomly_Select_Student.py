# Question 2 : Write a program that uses random.choice() to randomly select a student from a list and display the selected student's name.


# Import random module
import random

# Create a list of students
students = ["Ali", "Rahul", "John", "Summu", "Ayesha"]

# Select a random student
selected_student = random.choice(students)

# Display the selected student
print("The selected student for presentation is:", selected_student)
