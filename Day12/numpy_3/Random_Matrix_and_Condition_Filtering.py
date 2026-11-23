# 10. Random Matrix and Condition Filtering

# Scenario:
# ● Generate a 3×3 matrix of random numbers (0–50).

# Task:
# ● Filter elements greater than 25.
# ● Print filtered values.

# Import NumPy
import numpy as np

# Generate 3x3 random matrix
arr = np.random.randint(0, 51, (3, 3))

# Print original matrix
print("Original Matrix:")
print(arr)

# Filter values greater than 25
result = arr[arr > 25]

# Print filtered values
print("Values Greater Than 25:", result)