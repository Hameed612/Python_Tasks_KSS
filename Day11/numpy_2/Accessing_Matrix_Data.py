# 5. Accessing Matrix Data

# A teacher stores marks of students in two subjects:
# [[78, 85],
#  [90, 88],
#  [67, 72]]

# Task:
# ● Convert it to a NumPy array.
# ● Access the second student's second subject mark.

# Import NumPy
import numpy as np

# Store student marks
marks = [[78, 85],
         [90, 88],
         [67, 72]]

# Convert into NumPy array
arr = np.array(marks)

# Access second student's second subject
print("Second Student Second Subject:", arr[1, 1])