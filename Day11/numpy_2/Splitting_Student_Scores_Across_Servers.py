# 14. Splitting Student Scores Across Servers

# A dataset: [50, 60, 70, 80, 90, 100, 110, 120]

# Scenario:
# A distributed system needs to divide this data among 4 servers.

# Task:
# ● Convert to NumPy array.
# ● Split the array into 4 equal parts using array_split().

# Import NumPy
import numpy as np

# Store student scores
scores = [50, 60, 70, 80, 90, 100, 110, 120]

# Convert into NumPy array
arr = np.array(scores)

# Split array into 4 parts
result = np.array_split(arr, 4)

# Print each part
print("Server 1:", result[0])
print("Server 2:", result[1])
print("Server 3:", result[2])
print("Server 4:", result[3])