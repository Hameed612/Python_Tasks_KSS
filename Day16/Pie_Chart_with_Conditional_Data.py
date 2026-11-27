# 8. Pie Chart with Conditional Data

# Scenario:
# scores = np.array([40, 60, 80, 30, 90])

# Task:
# ● Categorize into:
# ○ Pass (>50)
# ○ Fail (<=50)
# ● Count using NumPy/Pandas
# ● Plot pie chart for Pass vs Fail

import numpy as np
import matplotlib.pyplot as plt

# Store student scores
scores = np.array([40, 60, 80, 30, 90])

# Count pass students
pass_count = np.sum(scores > 50)

# Count fail students
fail_count = np.sum(scores <= 50)

# Store counts
counts = [pass_count, fail_count]

# Store labels
labels = ["Pass", "Fail"]

# Print counts
print("Pass Students:", pass_count)
print("Fail Students:", fail_count)

# Create pie chart
plt.pie(counts, labels=labels, autopct="%1.1f%%")

# Add title
plt.title("Pass and Fail Students")

# Display chart
plt.show()