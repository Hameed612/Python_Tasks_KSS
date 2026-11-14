# Write a program that opens the file, reads all the contents, and displays them on the screen.

# Notes Reader Program

# Open the file in read mode
file = open("notes.txt", "r")

# Read all contents from the file
notes = file.read()

# Display notes on the screen
print("My Daily Notes:")
print(notes)

# Close the file
file.close()
