# 4. Conditional Discount System (List Comprehension)

# A shop has prices:
# prices = [100, 200, 300, 400]

# Scenario:
# ● Apply a 10% discount only if price > 200.

# Task:
# ● Use list comprehension with condition to create updated price list.

# Store product prices
prices = [100, 200, 300, 400]

# Apply 10% discount if price > 200
new_prices = [p * 0.9 if p > 200 else p for p in prices]

# Print updated prices
print("Original Prices:", prices)
print("Discount Prices:", new_prices)