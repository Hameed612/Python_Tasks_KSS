# 3. Product Rating System

# An e-commerce website stores product ratings: ratings = [4, 5, 3, 4, 2]

# Task:
# ● Convert it to a NumPy array.
# ● Print the first and last rating using indexing.

# Import NumPy
import numpy as np

# Store product ratings
ratings = [4, 5, 3, 4, 2]

# Convert into NumPy array
arr = np.array(ratings)

# Print first rating
print("First Rating:", arr[0])

# Print last rating
print("Last Rating:", arr[-1])