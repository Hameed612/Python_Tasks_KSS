# 5. Create a Number Guessing Game where:
#● The program generates a random number between 1 and 50 using random.
#● The user has 5 attempts to guess the number.
#● After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.


# Import random and math modules
import random
import math

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)

# Give the user 5 attempts
attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")
print("You have 5 attempts.")

# Repeat the game for 5 attempts
for i in range(attempts):

    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Calculate absolute difference
    difference = math.fabs(secret_number - guess)

    # Display the difference
    print("Difference from correct number:", difference)

    # Check whether the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess! Try again.")

# Display the correct number if attempts are over
else:
    print("Sorry! You have used all 5 attempts.")
    print("The correct number was:", secret_number)
