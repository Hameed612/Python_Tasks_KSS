# 6. Student Marks Analysis (NumPy → Pandas)

# Marks data:
# arr = np.array([
# [80, 90],
# [70, 60],
# [85, 95]
# ])

# Task:
# ● Convert into DataFrame with columns "Math", "Science"
# ● Add a new column Total
# ● Find student with highest total

# Import libraries
import numpy as np
import pandas as pd

# Create marks array
arr = np.array([
    [80, 90],
    [70, 60],
    [85, 95]
])

# Create DataFrame
df = pd.DataFrame(arr, columns=["Math", "Science"])

# Add Total column
df["Total"] = df["Math"] + df["Science"]

# Print DataFrame
print(df)

# Find highest total
print("Highest Total:", df["Total"].max())

# Find student with highest total
print(df.loc[df["Total"].idxmax()])