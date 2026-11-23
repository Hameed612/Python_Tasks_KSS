# 4. Product Rating Normalization

# Ratings from different users:
# ratings = np.array([2, 3, 4, 5, 1])

# Task:
# ● Normalize ratings to a range 0 to 1 using:
# normalized = (value - min) / (max - min)

# Product Rating Normalization

import numpy as np

# Create ratings array
ratings = np.array([2, 3, 4, 5, 1])

# Find minimum and maximum values
minimum = np.min(ratings)
maximum = np.max(ratings)

# Normalize ratings
normalized = (ratings - minimum) / (maximum - minimum)

# Print results
print("Original Ratings:", ratings)
print("Normalized Ratings:", normalized)