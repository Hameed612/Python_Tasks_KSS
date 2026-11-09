# 5. Dictionary Operations: Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.

students = {
    "Ram": 85,
    "Ameer": 90,
    "Pram": 80
}

# Add new student
students["Sneha"] = 95

# Update existing marks
students["Ram"] = 92

# Print all student details
for name, marks in students.items():
    print(name, ":", marks)
