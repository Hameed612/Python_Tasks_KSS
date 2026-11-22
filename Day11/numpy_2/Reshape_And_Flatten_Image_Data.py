# 15. Reshape and Flatten Image Data

# Scenario:
# An image is stored as a 2 × 3 matrix:
# [[1,2,3],
#  [4,5,6]]

# Task:
# 1. Convert it into a NumPy array.
# 2. Flatten the array into 1-D format.
# 3. Print the flattened array.

# Import NumPy
import numpy as np

# Store image data
image = [[1, 2, 3],
         [4, 5, 6]]

# Convert into NumPy array
arr = np.array(image)

# Flatten array into 1-D
result = arr.flatten()

# Print original array
print("Original Image:")
print(arr)

# Print flattened array
print("Flattened Image:")
print(result)