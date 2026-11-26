# 5. Employee Management System (OOP + File + Dict)

# Scenario:
# Manage employee data.

# Task:
# ● Create a class Employee
# ● Store employees in a dictionary
# ● Save data to a file
# ● Use exception handling for invalid salary input
# ● Use loop to display all employees


# Employee Management System

# Create Employee class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Display employee details
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


# Store employees in dictionary
employees = {}

try:

    # Add employee details
    n = int(input("Enter number of employees: "))

    for i in range(n):

        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))

        if salary < 0:
            print("Salary cannot be negative")
            continue

        emp = Employee(name, salary)

        employees[name] = emp

    # Display employees
    print("\nEmployee Details:")

    with open("employee.txt", "w") as file:

        for name, emp in employees.items():

            emp.display()

            # Save details in file
            file.write(name + " " + str(emp.salary) + "\n")

except ValueError:
    print("Invalid input! Enter correct values.")

print("Employee data saved!")
