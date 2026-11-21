# 6. Matrix Transformation in Image Processing
# An image processing system stores pixel intensity values in a matrix.

# Scenario:
# [[1, 2],
#  [3, 4]]

# Task:
# ● Create a NumPy array for this matrix.
# ● Find its transpose.
# ● Print both matrices.

# Matrix Transformation

import numpy as np

# Create a matrix
matrix = np.array([[1, 2],
                   [3, 4]])

# Find transpose
transpose = matrix.T

# Print both matrices
print("Original Matrix:")
print(matrix)

print("Transpose Matrix:")
print(transpose)