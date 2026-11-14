# A writer saves an article in a file called article.txt. Write a Python program that: Opens and reads the file  Counts the number of words, lines, and characters in the file Displays the results.

# Word Counter Program

# Open file in read mode
file = open("article.txt", "r")

# Read all contents
data = file.read()

# Count number of words
words = len(data.split())

# Count number of lines
lines = len(data.splitlines())

# Count number of characters
characters = len(data)

# Display results
print("Word Counter Results")

print("Total Words:", words)
print("Total Lines:", lines)
print("Total Characters:", characters)

# Close the file
file.close()
