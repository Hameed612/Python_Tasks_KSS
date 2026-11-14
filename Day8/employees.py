#Write a Python program to: 1. Read employee data from the file.
#2. Display all employee details.
#3. Find the employee with the highest salary.
#4. Append a new employee record to the file.


# Employee Salary Management System

# Open file in read mode
file = open("employees.txt", "r")

# Create empty list
employees = []

# Display employee details
print("Employee Details:")

# Read employee records
for line in file:

    # Separate name and salary
    name, salary = line.split()

    # Convert salary into integer
    salary = int(salary)

    # Store employee details
    employees.append((name, salary))

    # Display details
    print(name, salary)

# Close the file
file.close()

# Find highest salary employee
highest = max(employees, key=lambda x: x[1])

# Display highest salary
print("\nHighest Salary Employee:")
print("Name:", highest[0])
print("Salary:", highest[1])

# Open file in append mode
file = open("employees.txt", "a")

# Get new employee details
new_name = input("\n Enter employee name: ")
new_salary = int(input("\n Enter employee salary: "))

# Append new employee record
file.write(new_name + " " + str(new_salary) + "\n")

# Close the file
file.close()

# Display success message
print("\nNew Employee Added Successfully!")
