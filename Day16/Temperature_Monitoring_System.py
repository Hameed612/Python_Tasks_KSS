# 4. Temperature Monitoring System

# Scenario:
# temps = np.array([28, 30, 32, 35, 33, 31, 29])
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph → daily temperature trend
# ○ Bar chart → day-wise temperature
# ○ Pie chart → proportion of high (>30) vs low temps
# ○ Histogram → temperature frequency
# ○ Scatter plot → day index vs temperature

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store temperature data
temps = np.array([28, 30, 32, 35, 33, 31, 29])

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

# Display DataFrame
print(df)

# Create 5 graphs
plt.figure(figsize=(12, 8))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(df["Day"], df["Temperature"], marker="o")
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")

# 2. Bar chart
plt.subplot(2, 3, 2)
plt.bar(df["Day"], df["Temperature"])
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")

# 3. Pie chart
plt.subplot(2, 3, 3)

high = np.sum(temps > 30)
low = np.sum(temps <= 30)

plt.pie([high, low],
        labels=["High", "Low"],
        autopct="%1.1f%%")
plt.title("High vs Low Temperature")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(temps, bins=5)
plt.title("Temperature Frequency")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(range(len(temps)), temps)
plt.title("Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")

# Adjust spacing
plt.tight_layout()

# Display graphs
plt.show()