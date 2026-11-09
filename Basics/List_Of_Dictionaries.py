# 5. Perform employee data operations

# Create a list of employee dictionaries
employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# Find employee with highest salary
highest = max(employees, key=lambda x: x["salary"])

# Print highest salary employee
print("Highest Salary Employee:", highest)

# Filter employees with salary greater than 35000
print("\nEmployees with Salary Above 35000:")

for emp in employees:

    # Check salary condition
    if emp["salary"] > 35000:
        print(emp["name"], emp["salary"])

# Calculate total salary
total = 0

for emp in employees:
    total = total + emp["salary"]

# Calculate average salary
average = total / len(employees)

# Print average salary
print("\nAverage Salary:", average)

# Create a list of employee names
names = []

for emp in employees:
    names.append(emp["name"])

# Print employee names
print("\nEmployee Names:", names)
