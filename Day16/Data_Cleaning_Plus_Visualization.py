# 10. Data Cleaning + Visualization

# Scenario:
# data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Task:
# 1. Convert to Pandas Series
# 2. Replace NaN with mean
# 3. Plot:
# ○ Line graph of cleaned data
# ○ Bar chart of values > average

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store data with missing values
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert into Pandas Series
s = pd.Series(data)

# Calculate mean without NaN values
avg = s.mean()

# Replace NaN with mean
s = s.fillna(avg)

# Print cleaned data
print("Cleaned Data:")
print(s)

# Print average
print("Average:", avg)

# Create figure
plt.figure(figsize=(10, 4))

# First graph - Line graph
plt.subplot(1, 2, 1)
plt.plot(s, marker="o")
plt.title("Cleaned Data Line Graph")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid()

# Filter values greater than average
filtered = s[s > avg]

# Second graph - Bar chart
plt.subplot(1, 2, 2)
plt.bar(filtered.index, filtered.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")

# Adjust spacing
plt.tight_layout()

# Display graphs
plt.show()