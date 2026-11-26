# 4. Basic File Logger

# Scenario:
# A system logs user actions.

# Task:
# ● Take user input
# ● Store logs in a file
# ● Use loop to allow multiple entries
# ● Handle file errors using exception handling


# Basic File Logger

try:

    # Open file in append mode
    file = open("log.txt", "a")

    # Loop for multiple entries
    while True:

        action = input("Enter your action (stop to exit): ")

        # Stop the loop
        if action.lower() == "stop":
            break

        # Write action into file
        file.write(action + "\n")

        print("Log saved successfully!")

    file.close()

except IOError:
    print("File error occurred!")

print("Program completed")
