# 6. Multi-Level List Transformation (Advanced List Comprehension)

# A dataset contains:
# data = [[1, 2, 3], [4, 5], [6]]

# Task:
# ● Flatten the list using list comprehension.
# ● Then create a new list containing squares of only even numbers.

# Create nested list
data = [[1, 2, 3], [4, 5], [6]]

# Flatten the nested list
flat = [n for sublist in data for n in sublist]

# Find squares of even numbers
result = [n ** 2 for n in flat if n % 2 == 0]

# Print results
print("Flattened List:", flat)
print("Even Number Squares:", result)