# 9. Missing Data Handling (NumPy + Pandas)

# A dataset:
# arr = np.array([10, np.nan, 30, np.nan, 50])

# Task:
# ● Convert to Pandas Series
# ● Replace NaN values with the mean of the Series
# ● Print updated data

# Import libraries
import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([10, np.nan, 30, np.nan, 50])

# Convert into Series
S = pd.Series(arr)

# Find mean value
mean_value = S.mean()

# Replace NaN with mean
S = S.fillna(mean_value)

# Print updated Series
print(S)