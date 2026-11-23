# 6. Remove Outliers

# Given data:
# values = np.array([10, 12, 15, 18, 100, 14, 13])

# Task:
# ● Compute the mean and standard deviation
# ● Remove values that are more than 2 standard deviations from the mean.

# Remove Outliers

import numpy as np

# Create data array
values = np.array([10, 12, 15, 18, 100, 14, 13])

# Calculate mean
avg = np.mean(values)

# Calculate standard deviation
std = np.std(values)

# Set lower and upper limits
lower = avg - (2 * std)
upper = avg + (2 * std)

# Remove outliers
result = values[(values >= lower) & (values <= upper)]

# Print results
print("Mean:", avg)
print("Standard Deviation:", std)
print("Data after removing outliers:", result)