# 7. Filtered Bar Chart

# Scenario:
# marks = np.array([45, 80, 60, 30, 90])
# names = ["A", "B", "C", "D", "E"]

# Task:
# ● Convert to DataFrame
# ● Filter students with marks > 50
# ● Plot bar chart only for filtered students

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store marks and names
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Filter marks greater than 50
filtered = df[df["Marks"] > 50]

# Print filtered data
print(filtered)

# Plot bar chart
plt.bar(filtered["Name"], filtered["Marks"])

# Add labels and title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Scoring Above 50")

# Display graph
plt.show()