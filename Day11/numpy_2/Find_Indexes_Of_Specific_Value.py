# 10. Find Indexes of Specific Value

# A quality check system stores product defect codes: [2, 4, 1, 4, 3, 4, 5]

# Task:
# ● Find the indexes where value = 4 using NumPy searching.

# Import NumPy
import numpy as np

# Store defect codes
codes = [2, 4, 1, 4, 3, 4, 5]

# Convert into NumPy array
arr = np.array(codes)

# Find indexes where value is 4
result = np.where(arr == 4)

# Print indexes
print("Indexes:", result[0])