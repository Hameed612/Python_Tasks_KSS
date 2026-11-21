# 9. Multi-Department Data Aggregation
# A company collects employee counts from two branches.

# Branch A:
# [[10, 20],
#  [30, 40]]

# Branch B:
# [[5, 15],
#  [25, 35]]

# Scenario:
# ● Combine the two matrices.
# ● Calculate the total employees across all departments.
# ● Print the combined matrix and total.

# Multi-Department Data Aggregation

import numpy as np

# Create Branch A matrix
branch_a = np.array([[10, 20],
                     [30, 40]])

# Create Branch B matrix
branch_b = np.array([[5, 15],
                     [25, 35]])

# Combine both matrices vertically
combined = np.concatenate((branch_a, branch_b), axis=0)

# Calculate total employees
total = np.sum(combined)

# Print results
print("Combined Matrix:")
print(combined)

print("Total Employees:", total)