# 7. Splitting Data for Parallel Processing
# A dataset contains the following values:
# [5, 10, 15, 20, 25, 30]

# Scenario:
# You want to distribute the data across 3 processors.

# Task:
# ● Store the data in a NumPy array.
# ● Split it into 3 equal parts using NumPy.

# Splitting Data

import numpy as np

# Create dataset
data = np.array([5, 10, 15, 20, 25, 30])

# Split into 3 equal parts
result = np.split(data, 3)

# Print split arrays
print("Original Array:", data)

print("Split Arrays:")
for part in result:
    print(part)