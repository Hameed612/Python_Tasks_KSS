# 6. Check Data Type of Inventory Values

# A warehouse stores product quantities:
# [10, 20, 30, 40]

# Task:
# ● Convert it into a NumPy array.
# ● Print the data type (dtype) of the array.

# Import NumPy
import numpy as np

# Store product quantities
quantity = [10, 20, 30, 40]

# Convert into NumPy array
arr = np.array(quantity)

# Print array
print("Inventory:", arr)

# Print data type
print("Data Type:", arr.dtype)