
# Student Attendance Record

# Get student name from user
name = input("Enter student name: ")

# Open file in append mode
file = open("attendance.txt", "a")

# Write student name into file
file.write(name + "\n")

# Close the file
file.close()

# Open file in read mode
file = open("attendance.txt", "r")

# Display file contents
print("\nStudent Attendance Records:")
print(file.read())

# Close the file
file.close()
