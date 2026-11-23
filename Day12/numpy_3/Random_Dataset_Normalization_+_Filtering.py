# 12. Random Dataset Normalization + Filtering

# Scenario:
# ● Generate 8 random float values between 0 and 1.
# Task:
# 1. Normalize by multiplying with 100
# 2. Filter values greater than 50
# 3. Sort the filtered values

# Import NumPy
import numpy as np

# Generate 8 random float values
arr = np.random.rand(8)

# Normalize by multiplying with 100
normalized = arr * 100

# Filter values greater than 50
filtered = normalized[normalized > 50]

# Sort filtered values
result = np.sort(filtered)

# Print results
print("Original Values:", arr)
print("Normalized Values:", normalized)
print("Filtered Values:", filtered)
print("Sorted Values:", result)