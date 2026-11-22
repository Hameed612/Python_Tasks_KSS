# 4. Student Roll Numbers Extraction

# A list contains roll numbers:
# [101, 102, 103, 104, 105, 106]

# Scenario:
# You want only the middle students (index 2 to 4)

# Task:
# ● Use NumPy slicing to extract those values.

# Import NumPy
import numpy as np

# Store roll numbers
roll = [101, 102, 103, 104, 105, 106]

# Convert into NumPy array
arr = np.array(roll)

# Extract values from index 2 to 4
result = arr[2:5]

# Print result
print("Middle Roll Numbers:", result)