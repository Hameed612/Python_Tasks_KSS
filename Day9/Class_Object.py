# Create a Student class
class Student:
    name = "Hameed"
    roll_no = 101
    marks = 95

    # Method to display student details
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
    
# Create three student objects
s1 = Student()
s1.display()

s2 = Student()
s2.name = "Ali"
s2.roll_no = 102
s2.marks = 90
s2.display()

s3 = Student()
s3.name = "Kanyan"
s3.roll_no = 103
s3.marks = 78
s3.display()