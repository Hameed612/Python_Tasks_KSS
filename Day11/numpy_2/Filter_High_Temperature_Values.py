# 11. Filter High Temperature Values

# A weather station records temperatures:
# [28, 31, 35, 27, 40, 22]

# Scenario:
# The system needs temperatures above 30°C.

# Task:
# ● Filter the values greater than 30 using NumPy boolean filtering.

# Import NumPy
import numpy as np

# Store temperature values
temp = [28, 31, 35, 27, 40, 22]

# Convert into NumPy array
arr = np.array(temp)

# Filter values greater than 30
result = arr[arr > 30]

# Print filtered temperatures
print("High Temperatures:", result)