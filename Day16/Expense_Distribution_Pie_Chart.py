# 3. Expense Distribution Pie Chart

# Scenario:
# Monthly expenses:
# expenses = np.array([500, 300, 200])
# labels = ["Food", "Rent", "Travel"]

# Task:
# ● Create a pie chart
# ● Show percentage distribution

import numpy as np
import matplotlib.pyplot as plt

# Store expense data
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# Create pie chart
plt.pie(expenses, labels=labels, autopct="%1.1f%%")

# Add title
plt.title("Monthly Expenses")

# Display chart
plt.show()