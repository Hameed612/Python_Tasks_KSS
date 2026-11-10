# Question 4 : Write a Python program that generates 20 random numbers between 1 and 200 using the random module and stores them in a list.

# Import random and math modules
import random
import math

# Create an empty list
numbers = []

# Generate 20 random numbers
for i in range(20):
    num = random.randint(1, 200)
    numbers.append(num)

# Display the list
print("Random numbers:", numbers)

# Find maximum and minimum values
maximum = max(numbers)
minimum = min(numbers)

# Calculate square root of maximum
square_root = math.sqrt(maximum)

# Calculate logarithm of minimum
log_value = math.log(minimum)

# Display the results
print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Square root of maximum:", square_root)
print("Logarithm of minimum:", log_value)
