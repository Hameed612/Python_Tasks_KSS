# 1. Fruit Sales Comparison (Series Addition)

# A shop tracks fruit sales:
# S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
# S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])

# Task:
# ● Add both series
# ● Find the total sales of all fruits combined

# Import pandas
import pandas as pd

# Create first Series
S1 = pd.Series([10, 20, 30],
               index=["apple", "banana", "cherry"])

# Create second Series
S2 = pd.Series([5, 15, 25],
               index=["apple", "banana", "cherry"])

# Add both Series
total = S1 + S2

# Display total sales of each fruit
print("Fruit Sales:")
print(total)

# Calculate combined sales
print("Total Sales:", total.sum())