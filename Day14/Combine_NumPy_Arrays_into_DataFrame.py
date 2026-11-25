# 8. Combine NumPy Arrays into DataFrame

# Two arrays:
# names = np.array(["A", "B", "C"])
# marks = np.array([80, 90, 70])

# Task:
# ● Create a DataFrame with columns "Name" and "Marks"
# ● Filter students with marks above 75

# Import libraries
import numpy as np
import pandas as pd

# Create arrays
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Print DataFrame
print(df)

# Filter marks above 75
result = df[df["Marks"] > 75]

# Print filtered students
print("Students above 75:")
print(result)