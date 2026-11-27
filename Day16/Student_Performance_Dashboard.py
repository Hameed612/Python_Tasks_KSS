# 1. Student Performance Dashboard

# Scenario:
# A school records marks of students in one subject:
# marks = np.array([45, 67, 89, 56, 72, 91, 38])
# students = ["A", "B", "C", "D", "E", "F", "G"]

# Task:
# ● Convert to Pandas DataFrame
# ● Plot:
# ○ Line graph → trend of marks
# ○ Bar chart → student vs marks
# ○ Pie chart → Pass (>50) vs Fail
# ○ Histogram → distribution of marks
# ○ Scatter plot → index vs marks

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store student marks
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

# Display DataFrame
print(df)

# Create 5 graphs
plt.figure(figsize=(12, 8))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(df["Student"], df["Marks"], marker="o")
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")

# 2. Bar chart
plt.subplot(2, 3, 2)
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks")

# 3. Pie chart
plt.subplot(2, 3, 3)

passed = np.sum(marks > 50)
failed = np.sum(marks <= 50)

plt.pie([passed, failed],
        labels=["Pass", "Fail"],
        autopct="%1.1f%%")
plt.title("Pass vs Fail")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")

# Adjust spacing
plt.tight_layout()

# Display all graphs
plt.show()