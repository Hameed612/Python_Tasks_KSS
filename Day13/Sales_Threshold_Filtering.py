# 1. Sales Threshold Filtering

# You are given monthly sales:
# sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

# Task:
# ● Filter all sales values greater than the average sales
# ● Return the filtered array.

# Sales Threshold Filtering

import numpy as np

# Create sales array
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

# Calculate average sales
avg = np.mean(sales)

# Filter sales greater than average
result = sales[sales > avg]

# Print results
print("Average Sales:", avg)
print("Sales greater than average:", result)