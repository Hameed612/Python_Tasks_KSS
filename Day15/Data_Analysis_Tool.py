# 6. Data Analysis Tool (NumPy + Pandas)

# Scenario:
# Analyze student marks.

# Task:
# ● Generate marks using NumPy
# ● Convert into Pandas DataFrame
# ● Use conditions to filter passing students
# ● Calculate mean using math/NumPy
# ● Use loop to print results


# Data Analysis Tool

import numpy as np
import pandas as pd

# Generate student marks
marks = np.array([80, 45, 90, 35, 70])

# Student names
names = ["Rahul", "Anita", "Ravi", "Priya", "John"]

# Create DataFrame
data = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Student Data:")
print(data)

# Filter passing students
# Passing marks are 40 and above
passed = data[data["Marks"] >= 40]

print("\nPassed Students:")
print(passed)

# Calculate average
average = np.mean(marks)

print("\nAverage Marks:", average)

# Print results using loop
print("\nStudent Results:")

for i in range(len(names)):

    if marks[i] >= 40:
        print(names[i], "Pass")
    else:
        print(names[i], "Fail")
