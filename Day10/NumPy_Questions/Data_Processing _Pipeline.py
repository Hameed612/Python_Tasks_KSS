# 10. Data Processing Pipeline

# A data pipeline receives the following array:
# [12, 7, 25, 3, 18, 10]

# Scenario:
# 1. Convert the list into a NumPy array.
# 2. Sort the array.
# 3. Split the sorted array into two equal parts.
# 4. Calculate the sum of each part.

# Output:
# ● Sorted array
# ● Two split arrays
# ● Sum of each part.

# Data Processing Pipeline

import numpy as np

# Create data list
data = [12, 7, 25, 3, 18, 10]

# Convert list into NumPy array
arr = np.array(data)

# Sort the array
sorted_arr = np.sort(arr)

# Split into two equal parts
parts = np.split(sorted_arr, 2)

# Calculate sum of each part
sum1 = np.sum(parts[0])
sum2 = np.sum(parts[1])

# Print results
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)

print("First Split:", parts[0])
print("Second Split:", parts[1])

print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)