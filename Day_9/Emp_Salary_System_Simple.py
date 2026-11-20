# Question: Create an Employee base class and a Manager derived class. Display employee details.

# Parent class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Child class
class Manager(Employee):

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


# Create Manager object
m1 = Manager("Hameed", 30000)

# Display details
m1.display()