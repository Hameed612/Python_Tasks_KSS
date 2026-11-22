# 8. Iterate Through Daily Sales

# Daily sales data:
# [200, 300, 150, 400]

# Task:
# ● Store it in a NumPy array.
# ● Iterate through the array and print each sale value.

# Import NumPy
import numpy as np

# Store daily sales
sales = [200, 300, 150, 400]

# Convert into NumPy array
arr = np.array(sales)

# Iterate through array
for value in arr:
    print(value)