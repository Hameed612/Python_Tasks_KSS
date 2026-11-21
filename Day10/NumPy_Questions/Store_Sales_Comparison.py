# 5. Store Sales Comparison
# Two stores record daily sales for 3 days.

# Scenario:
# Store A = [200, 250, 300]
# Store B = [180, 270, 310]

# Task:
# ● Store them in NumPy arrays.
# ● Find the daily difference in sales between the two stores.
# ● Print the resulting array.

# Store Sales Comparison

import numpy as np

# Create sales arrays
store_a = np.array([200, 250, 300])
store_b = np.array([180, 270, 310])

# Calculate daily difference
difference = store_a - store_b

# Print results
print("Store A Sales:", store_a)
print("Store B Sales:", store_b)
print("Sales Difference:", difference)