# 2. Even Number Filter (List Comprehension)

# A system stores numbers:
# nums = [1, 2, 3, 4, 5, 6]
# Task:
# Use list comprehension to create a new list containing only even numbers.

# Store numbers in a list
nums = [1, 2, 3, 4, 5, 6]

# Create a new list containing even numbers
even = [n for n in nums if n % 2 == 0]

# Print even numbers
print("Even Numbers:", even)