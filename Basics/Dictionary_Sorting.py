# 4: Sort students based on marks

# Create student dictionary
students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}

# Sort dictionary based on marks in descending order
sorted_students = sorted(
    students.items(),
    key=lambda x: x[1],
    reverse=True
)

# Print sorted student details
print("Students Sorted by Marks:")

for name, marks in sorted_students:
    print(name, ":", marks)

# Print top two students
print("\nTop Two Students:")

for name, marks in sorted_students[:2]:
    print(name, ":", marks)
