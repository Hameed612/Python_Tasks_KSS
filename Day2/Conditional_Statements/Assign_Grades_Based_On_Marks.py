# Question 5: Write a Python program to assign grades based on marks using if-elif-else (A, B, C, or Fail).

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("Fail")
