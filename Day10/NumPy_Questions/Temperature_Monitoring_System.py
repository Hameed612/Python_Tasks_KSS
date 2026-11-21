# 2. Temperature Monitoring System
# A weather station records temperatures for two days.

# Scenario:
# Day 1: [30, 32, 31]
# Day 2: [29, 33, 34]

# Task:
# ● Create a 2D NumPy array to store this data.
# ● Print the array.
# ● Find the total temperature recorded.

# Temperature Monitoring System

import numpy as np

# Create temperature data
temp = np.array([[30, 32, 31],
                 [29, 33, 34]])

# Print temperature array
print("Temperature Data:")
print(temp)

# Calculate total temperature
total = np.sum(temp)

print("Total Temperature:", total)