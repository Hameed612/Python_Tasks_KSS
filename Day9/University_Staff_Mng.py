# Parent class
class Staff:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Child class 1
class Professor(Staff):

    def display(self):
        print("Professor:", self.name)
        print("Salary:", self.salary)


# Child class 2
class LabAssistant(Staff):

    def display(self):
        print("Lab Assistant:", self.name)
        print("Salary:", self.salary)


# Child class 3
class Administrator(Staff):

    def display(self):
        print("Administrator:", self.name)
        print("Salary:", self.salary)


# Create objects
p = Professor("Rahul", 50000)
l = LabAssistant("Anita", 25000)
a = Administrator("Ravi", 35000)

# Display details
p.display()
l.display()
a.display()