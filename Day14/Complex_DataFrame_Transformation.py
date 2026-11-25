# 8. Complex DataFrame Transformation

# A DataFrame:
# df = pd.DataFrame({
#     "Name": ["A", "B", "C", "D"],
#     "Marks": [50, 80, 30, 90]
# })

# Scenario:
# ● Students scoring below 50 failed

# Task:
# 1. Create a column Status ("Pass"/"Fail")
# 2. Filter only passed students
# 3. Calculate average marks of passed students

# Import pandas
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# Create Status column
df["Status"] = df["Marks"].apply(
    lambda x: "Fail" if x < 50 else "Pass"
)

# Display all student details
print("Student Details:")
print(df)

# Filter passed students
passed = df[df["Status"] == "Pass"]

# Display passed students
print("Passed Students:")
print(passed)

# Calculate average marks
average = passed["Marks"].mean()

# Display average marks
print("Average Marks of Passed Students:", average)