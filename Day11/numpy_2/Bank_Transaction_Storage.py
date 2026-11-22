# 1. Bank Transaction Storage

# A bank stores the transaction amounts of a customer in a list:
# transaction_amounts = [1200, 500, 800, 1500]

# Scenario:
# ● Convert the list into a NumPy array.
# ● Print the type of the object.
# ● Verify that it is a NumPy ndarray.

# Import NumPy
import numpy as np

# Store transaction amounts in a list
amounts = [1200, 500, 800, 1500]

# Convert list into NumPy array
arr = np.array(amounts)

# Print array
print("Transaction Array:", arr)

# Print object type
print("Type:", type(arr))

# Check whether it is NumPy ndarray
print("Is ndarray:", isinstance(arr, np.ndarray))