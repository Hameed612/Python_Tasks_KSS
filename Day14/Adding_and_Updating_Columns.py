# 5. Adding and Updating Columns

# A DataFrame:
# df = pd.DataFrame({
#     "Price": [100, 200, 300]
# })

# Scenario:
# ● Add a column Discount = 10% of Price
# ● Add another column Final Price = Price - Discount

# Import pandas
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Price": [100, 200, 300]
})

# Calculate 10% discount
df["Discount"] = df["Price"] * 10 / 100

# Calculate final price
df["Final Price"] = df["Price"] - df["Discount"]

# Display updated DataFrame
print("Product Details:")
print(df)