# Write a Python program that takes multiple items from the user and writes them into the file, with each item on a new line

# Grocery List Manager

# Open file in write mode
file = open("grocery.txt", "w")

# Get number of grocery items
n = int(input("How many items do you want to add? "))

# Get grocery items using for loop
for i in range(n):

    # Enter item name
    item = input("Enter grocery item: ")

    # Write item into file
    file.write(item + "\n")

# Close the file
file.close()

# Display success message
print("\nGrocery items saved successfully!")

# Open file in read mode
file = open("grocery.txt", "r")

# Display grocery list
print("\nMy Grocery List:")
print(file.read())

# Close the file
file.close()
