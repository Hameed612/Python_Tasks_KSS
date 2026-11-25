# 5. Filter Values Using Condition

# A dataset:
# arr = np.array([10, 25, 30, 15, 40])

# Task:
# ● Convert to Pandas Series
# ● Filter values greater than 20

# Import libraries
import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([10, 25, 30, 15, 40])

# Convert into Series
S = pd.Series(arr)

# Filter values greater than 20
result = S[S > 20]

# Print result
print(result)