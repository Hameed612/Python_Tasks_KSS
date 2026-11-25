# 1. Convert NumPy Array to Pandas Series

# A dataset:
# arr = np.array([10, 20, 30, 40])
# Task:
# ● Convert this NumPy array into a Pandas Series
# ● Assign index labels: ["A", "B", "C", "D"]

# Import libraries
import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([10, 20, 30, 40])

# Convert array into Series
S = pd.Series(arr, index=["A", "B", "C", "D"])

# Print Series
print(S)