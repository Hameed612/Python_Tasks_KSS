# 3. Accessing Specific Data (Indexing)

# A Series contains:
# S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])

# Task:
# ● Access values for B and D
# ● Return them as a subset

# Import pandas
import pandas as pd

# Create Series
S = pd.Series([100, 200, 300, 400],
              index=["A", "B", "C", "D"])

# Access value B
print("Value of B:", S["B"])

# Access value D
print("Value of D:", S["D"])

# Create subset using B and D
result = S[["B", "D"]]

# Display subset
print("Selected Data:")
print(result)