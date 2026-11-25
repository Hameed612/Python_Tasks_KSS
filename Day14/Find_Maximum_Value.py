# 4. Find Maximum Value

# A dataset:
# arr = np.array([12, 45, 22, 67, 34])

# Task:
# ● Convert to Pandas Series
# ● Find the maximum value

# Import libraries
import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([12, 45, 22, 67, 34])

# Convert into Series
S = pd.Series(arr)

# Find maximum value
print("Maximum Value:", S.max())