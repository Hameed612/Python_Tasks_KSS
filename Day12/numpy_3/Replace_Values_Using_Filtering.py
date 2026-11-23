# 9. Replace Values Using Filtering

# Scenario:
# A dataset contains: [5, 12, 18, 7, 25, 30]

# Task:
# ● Replace all values greater than 15 with 0 using NumPy filtering.

# Import NumPy
import numpy as np

# Create array
arr = np.array([5, 12, 18, 7, 25, 30])

# Replace values greater than 15 with 0
arr[arr > 15] = 0

# Print updated array
print("Updated Array:", arr)