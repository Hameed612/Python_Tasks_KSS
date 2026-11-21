# 3. Sorting Product Prices
# An e-commerce company stores product prices in a NumPy array.

# Scenario:
# Prices = [499, 299, 799, 199, 599]

# Task:
# ● Convert it into a NumPy array.
# ● Sort the prices in ascending order.

# Sorting Product Prices

import numpy as np

# Create product price list
prices = [499, 299, 799, 199, 599]

# Convert into NumPy array
arr = np.array(prices)

# Sort prices
sorted_prices = np.sort(arr)

# Print sorted prices
print("Original Prices:", arr)
print("Sorted Prices:", sorted_prices)