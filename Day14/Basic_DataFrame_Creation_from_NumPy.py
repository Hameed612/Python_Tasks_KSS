# 2. Basic DataFrame Creation from NumPy

# You have:
# data = np.array([[1, 2], [3, 4], [5, 6]])

# Task:
# ● Convert it into a Pandas DataFrame
# ● Add column names: "X", "Y"

# Import libraries
import numpy as np
import pandas as pd

# Create NumPy array
data = np.array([[1, 2], [3, 4], [5, 6]])

# Convert into DataFrame
df = pd.DataFrame(data, columns=["X", "Y"])

# Print DataFrame
print(df)