# 2. Student Marks Analysis

# Given marks of 5 students in 3 subjects:
# marks = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [50, 65, 70],
#     [90, 95, 85],
#     [40, 55, 60]

# ])

# Task:
# ● Calculate total marks of each student.
# ● Identify students whose total marks are above the class average.

# Student Marks Analysis

import numpy as np

# Create marks array
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

# Calculate total marks of each student
total = np.sum(marks, axis=1)

# Calculate class average
avg = np.mean(total)

# Find students above average
result = total[total > avg]

# Print results
print("Total Marks:", total)
print("Class Average:", avg)
print("Above Average Marks:", result)