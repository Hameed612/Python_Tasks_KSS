# 4. Temperature Trend Line Plot

# Scenario:
# Daily temperatures:
# temps = np.array([28, 30, 32, 31, 29])

# Task:
# ● Convert into Pandas Series
# ● Plot a line graph
# ● Add title and grid

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store temperature data
temps = np.array([28, 30, 32, 31, 29])

# Convert into Pandas Series
s = pd.Series(temps)

# Print Series
print(s)

# Plot line graph
plt.plot(s, marker="o")

# Add title and labels
plt.title("Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")

# Show grid
plt.grid()

# Display graph
plt.show()