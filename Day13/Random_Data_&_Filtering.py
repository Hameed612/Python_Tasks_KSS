# 8. Random Data & Filtering

# Generate random numbers:
# nums = np.random.randint(1, 100, 10)

# Task:
# ● Filter values that are divisible by 5
# ● Return sorted result.

# Random Data and Filtering

import numpy as np

# Generate 10 random numbers between 1 and 99
nums = np.random.randint(1, 100, 10)

# Filter numbers divisible by 5
result = nums[nums % 5 == 0]

# Sort the filtered numbers
result = np.sort(result)

# Print results
print("Random Numbers:", nums)
print("Numbers Divisible by 5:", result)