
# Student Marks Management System

# Tuple: Store subject names
subjects = ("Math", "Science", "English")

# Set: Store unique student names
student_names = set()

# Dictionary: Store student names and marks
students = {}


# Function 1: Add student details
def add_student():

    name = input("Enter student name: ")

    # Check duplicate student name
    if name in student_names:
        print("Student already exists!")
        return

    marks = []

    try:
        # Get marks for three subjects
        for subject in subjects:
            mark = float(input("Enter marks for " + subject + ": "))
            marks.append(mark)

        # Store marks in dictionary
        students[name] = marks

        # Add student name to set
        student_names.add(name)

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")


# Function 2: Display all student records
def display_students():

    if len(students) == 0:
        print("No student records found.")

    else:
        print("\nStudent Records:")

        for name, marks in students.items():
            print(name, ":", marks)


# Function 3: Recursive function to calculate total marks
def calculate_total(marks):

    # Check marks data type
    if not isinstance(marks, list):
        raise TypeError

    # Base condition
    if len(marks) == 0:
        return 0

    # Recursive condition
    if not isinstance(marks[0], (int, float)):
        raise TypeError

    return marks[0] + calculate_total(marks[1:])


# Function 4: Calculate student average
def calculate_average():

    try:
        name = input("Enter student name to calculate average: ")

        # Check whether student exists
        if name not in students:
            raise NameError

        marks = students[name]

        # Calculate total using recursion
        total = calculate_total(marks)

        # Calculate average
        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")


# Main Menu
while True:

    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Please enter a valid menu number.")
