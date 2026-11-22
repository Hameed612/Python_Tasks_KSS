# 12. Sorting Customer Names

# A system stores customer names:
# ["Ravi", "Anil", "Sita", "John"]
# Task:
# ● Convert it to a NumPy array.
# ● Sort the names alphabetically.

# Import NumPy
import numpy as np

# Store customer names
names = ["Hameed", "Anil", "Hemant", "Kalyan"]

# Convert into NumPy array
arr = np.array(names)

# Sort names alphabetically
result = np.sort(arr)

# Print sorted names
print("Sorted Names:", result)