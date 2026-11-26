# 3. Shopping Cart System

# Scenario: A user adds items to a shopping cart.

# Task:
# ● Store items in a list
# ● Convert to set to remove duplicates
# ● Use loop + condition to calculate total cost
# ● Handle invalid input using try-except


# Shopping Cart System

# Store product prices
prices = {
    "apple": 20,
    "banana": 10,
    "mango": 30,
    "orange": 15
}

# Shopping cart
cart = []

# Take user input
n = int(input("How many items do you want? "))

for i in range(n):
    item = input("Enter item name: ").lower()
    cart.append(item)

# Remove duplicate items
unique_cart = set(cart)

print("\nShopping Cart:", unique_cart)

total = 0

# Calculate total cost
for item in unique_cart:

    if item in prices:
        total = total + prices[item]
        print(item, "=", prices[item])

    else:
        print(item, "is not available")

print("Total Bill:", total)
