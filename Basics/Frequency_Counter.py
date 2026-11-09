# Frequency Counter: Given a string "programming", create a dictionary that counts how many times each character appears.

# Program 7: Count frequency of each character

# Create a string
text = "programming"

# Create an empty dictionary
frequency = {}

# Check each character
for char in text:

    # If character already exists, increase count
    if char in frequency:
        frequency[char] += 1

    # Otherwise, initialize count as 1
    else:
        frequency[char] = 1

# Print character frequency
print("Character Frequency:", frequency)
