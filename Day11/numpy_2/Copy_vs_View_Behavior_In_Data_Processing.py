# 13. Copy vs View Behavior in Data Processing

# Scenario:
# A dataset: [10, 20, 30, 40]

# Task:
# ● Create a copy of the array.
# ● Modify the original array.
# ● Show that the copy does not change.
# ● Repeat using view() and observe the difference.

# Import NumPy
import numpy as np

# Create original array
arr = np.array([10, 20, 30, 40])

# Create a copy
copy_arr = arr.copy()

# Create a view
view_arr = arr.view()

# Modify original array
arr[0] = 100

# Print all arrays
print("Original Array:", arr)
print("Copy Array:", copy_arr)
print("View Array:", view_arr)