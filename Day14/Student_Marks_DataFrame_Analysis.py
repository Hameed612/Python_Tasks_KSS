# 4. Student Marks DataFrame Analysis

# A DataFrame:
# data = pd.DataFrame({
#     "Name": ["A", "B", "C"],
#     "Math": [80, 70, 60],
#     "Science": [90, 60, 70]
# })

# Task:
# ● Add a new column Total = Math + Science
# ● Find the student with the highest total marks

# Import pandas
import pandas as pd

# Create DataFrame
data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

# Calculate total marks
data["Total"] = data["Math"] + data["Science"]

# Display DataFrame
print("Student Marks:")
print(data)

# Find student with highest marks
highest = data.loc[data["Total"].idxmax()]

# Display highest scorer
print("Highest Scoring Student:")
print(highest)