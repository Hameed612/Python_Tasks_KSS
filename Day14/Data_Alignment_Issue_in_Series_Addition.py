# 7. Data Alignment Issue in Series Addition

# Two Series:
# S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
# S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

# Task:
# ● Add both Series
# ● Explain why some values become NaN
# ● Replace NaN with 0 and compute final result

# Import pandas
import pandas as pd

# Create first Series
S1 = pd.Series([10, 20, 30],
               index=["a", "b", "c"])

# Create second Series
S2 = pd.Series([5, 15, 25],
               index=["b", "c", "d"])

# Add both Series
result = S1 + S2

# Display original result
print("Series Addition:")
print(result)

# Replace NaN with 0
result = result.fillna(0)

# Display final result
print("Final Result:")
print(result)