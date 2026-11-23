# 7. Filter Positive Even Numbers from Dataset

# Scenario:
# A dataset contains mixed values:
# arr = [-5, 10, 15, -2, 20, 25, 30]
# Task:
# ● Convert to NumPy array.
# ● Filter values that are:
# ○ Positive
# ○ Even

# Import NumPy
import numpy as np

# Store mixed numbers
arr = np.array([-5, 10, 15, -2, 20, 25, 30])

# Filter positive and even numbers
result = arr[(arr > 0) & (arr % 2 == 0)]

# Print result
print("Positive Even Numbers:", result)
