# 17. Employee Bonus Calculator (Decorators & OOP)
# A company wants to apply a bonus calculation automatically before displaying the
# salary. Create an Employee class and use a decorator that modifies the salary by
# adding a bonus before displaying it.

# Create a decorator
def add_bonus(func):

    def wrapper(self):

        # Add bonus to employee salary
        bonus = 5000
        total_salary = self.salary + bonus

        # Display salary with bonus
        print("Employee Name:", self.name)
        print("Original Salary:", self.salary)
        print("Bonus Amount:", bonus)

        # Call original function with updated salary
        func(self, total_salary)

    return wrapper


# Create Employee class
class Employee:

    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Apply decorator
    @add_bonus
    def display_salary(self, total_salary):

        print("Final Salary:", total_salary)


# Create employee object
e1 = Employee("Hameed", 30000)

# Display salary with bonus
e1.display_salary()