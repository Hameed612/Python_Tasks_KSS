# 6. Multi-Line Graph for Sales Comparison

# Scenario:
# data = {
# "Month": ["Jan", "Feb", "Mar"],
# "Store_A": [100, 150, 200],
# "Store_B": [90, 140, 210]
# }

# Task:
# ● Create DataFrame
# ● Plot two line graphs on same plot
# ● Add legend

import pandas as pd
import matplotlib.pyplot as plt

# Store sales data
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Plot Store A
plt.plot(df["Month"], df["Store_A"],
         marker="o", label="Store A")

# Plot Store B
plt.plot(df["Month"], df["Store_B"],
         marker="o", label="Store B")

# Add labels and title
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Comparison")

# Show legend
plt.legend()

# Display graph
plt.show()