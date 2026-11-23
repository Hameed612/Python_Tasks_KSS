# 5. Reshape & Row Averages

# A dataset:
# data = np.arange(1, 13)

# Task:
# ● Reshape it into a 3×4 matrix
# ● Compute average of each row

# Reshape and Row Averages

import numpy as np

# Create numbers from 1 to 12
data = np.arange(1, 13)

# Reshape into 3 rows and 4 columns
matrix = data.reshape(3, 4)

# Calculate average of each row
result = np.mean(matrix, axis=1)

# Print results
print("3x4 Matrix:")
print(matrix)

print("Row Averages:", result)