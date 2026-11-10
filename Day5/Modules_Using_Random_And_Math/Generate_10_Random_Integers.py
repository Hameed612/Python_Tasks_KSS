# Question 1: Write a Python program using the random module to generate 10 random integers between 1 and 100 and store them in a list. Print the list.

# Import random module
import random

# Create an empty list
numbers = []

# Generate 10 random integers
for i in range(10):
    num = random.randint(1, 100)
    numbers.append(num)

# Display the list
print("List of 10 random numbers:", numbers)
