# Import functions from utilities package

from utilities.math_operations import addition, multiplication
from utilities.string_operations import uppercase, count_characters

# Get two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform addition
print("Addition:", addition(num1, num2))

# Perform multiplication
print("Multiplication:", multiplication(num1, num2))

# Get a string from the user
text = input("Enter a string: ")

# Convert string into uppercase
print("Uppercase:", uppercase(text))

# Count characters
print("Character count:", count_characters(text))
