# 8. Write a program to find the student with the highest marks from a dictionary.

students = {
    "Hameed": 95,
    "Rahul": 90,
    "Arun": 85
}

topper = max(students, key=students.get)

print("Topper:", topper)
print("Highest Marks:", students[topper])
