# 10. Row Filtering + Aggregation

# A dataset:
# arr = np.array([
#     [100, 200],
#     [150, 250],
#     [80, 120],
#     [300, 400]
# ])

# Task:
# ● Convert to DataFrame with columns "Sales", "Profit"
# ● Filter rows where Sales > 100
# ● Find average Profit of filtered rows

# Import libraries
import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

# Convert into DataFrame
df = pd.DataFrame(arr, columns=["Sales", "Profit"])

# Filter Sales greater than 100
result = df[df["Sales"] > 100]

# Print filtered rows
print(result)

# Find average Profit
avg = result["Profit"].mean()

# Print average Profit
print("Average Profit:", avg)