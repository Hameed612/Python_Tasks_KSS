# Write a Python program to:
# Read the file
# Display all student records
# Calculate and display the average marks of the class
# Student Marks File Analyzer

# Open the file in read mode
file = open("marks.txt", "r")

# Initialize total and count
total = 0
count = 0

# Display heading
print("Student Records:")

# Read file line by line
for line in file:

    # Split name and marks
    name, marks = line.split()

    # Convert marks into integer
    marks = int(marks)

    # Display student details
    print(name, marks)

    # Calculate total marks
    total = total + marks

    # Count students
    count = count + 1

# Calculate average marks
average = total / count

# Display average
print("\nTotal Marks:", total)
print("Average Marks:", average)

# Close the file
file.close()
