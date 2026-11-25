# 7. Replace Values Using NumPy + Pandas

# A Series:
# S = pd.Series([10, 50, 30, 80, 20])
# Task:
# ● Replace values greater than 40 with 0 using NumPy logic
# ● Return updated Series

# Import libraries
import numpy as np
import pandas as pd

# Create Series
S = pd.Series([10, 50, 30, 80, 20])

# Replace values greater than 40 with 0
S[S > 40] = 0

# Print updated Series
print(S)