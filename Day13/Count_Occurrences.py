# 7. Count Occurrences

# You have:
# data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

# Task:
# ● Count how many times each unique number appears.
# ● Return numbers with their counts.

# Count Occurrences

import numpy as np

# Create data array
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

# Find unique numbers and their counts
numbers, counts = np.unique(data, return_counts=True)

# Print results
print("Unique Numbers:", numbers)
print("Counts:", counts)

# Display each number with its count
for i in range(len(numbers)):
    print(numbers[i], "appears", counts[i], "times")