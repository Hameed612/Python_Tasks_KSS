# Question 3 : Write a Python program using the math module to calculate and display the square root, floor value, and ceiling value of a number entered by the user.


# Import math module
import math

# Get a number from the user
num = float(input("Enter a number: "))

# Calculate square root
square_root = math.sqrt(num)

# Calculate floor value
floor_value = math.floor(num)

# Calculate ceiling value
ceiling_value = math.ceil(num)

# Display the results
print("Square root:", square_root)
print("Floor value:", floor_value)
print("Ceiling value:", ceiling_value)
