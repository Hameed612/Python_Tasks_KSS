# 7. Convert Float Prices to Integer

# A shop stores product prices: prices = [10.5, 20.8, 15.3]

# Scenario:
# The billing system requires integer values.

# Task:
# ● Convert the array from float to integer using astype().

# Import NumPy
import numpy as np

# Store product prices
prices = [10.5, 20.8, 15.3]

# Convert into NumPy array
arr = np.array(prices)

# Convert float into integer
new_arr = arr.astype(int)

# Print original array
print("Original Prices:", arr)

# Print integer array
print("Integer Prices:", new_arr)