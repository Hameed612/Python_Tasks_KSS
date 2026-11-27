# 2. Student Marks Bar Chart

# Scenario:
# Marks of students:
# names = ["A", "B", "C", "D"]
# marks = np.array([70, 85, 60, 90])

# Task:
# ● Create a DataFrame
# ● Plot a bar graph
# ● Show student names on X-axis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store student names and marks
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Print DataFrame
print(df)

# Plot bar chart
plt.bar(df["Name"], df["Marks"])

# Add labels and title
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Student Marks")

# Display graph
plt.show()