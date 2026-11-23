# 3. Temperature Alert System

# Temperatures recorded in a city:
# temps = np.array([28, 32, 35, 31, 29, 40, 38])

# Task:
# ● Identify days where temperature is greater than 30.
# ● Return their indices.

# Temperature Alert System

import numpy as np

# Create temperature array
temps = np.array([28, 32, 35, 31, 29, 40, 38])

# Find indices where temperature is greater than 30
result = np.where(temps > 30)

# Print results
print("Temperatures:", temps)
print("Day Indices:", result[0])