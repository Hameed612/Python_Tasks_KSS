# 1. Student Marks Analysis
# A teacher stores the marks of 5 students in a NumPy array.

# Scenario:
# You are given marks [45, 67, 89, 56, 72].

# Task:
#● Convert the list into a NumPy array.
#● Add 5 grace marks to every student.
#● Print the updated marks.

# Student Marks Analysis

import numpy as np

# Create a list of student marks
marks = [45, 67, 89, 56, 72]

# Convert list into NumPy array
arr = np.array(marks)

# Add 5 grace marks
updated_marks = arr + 5

# Print updated marks
print("Original Marks:", arr)
print("Updated Marks:", updated_marks)