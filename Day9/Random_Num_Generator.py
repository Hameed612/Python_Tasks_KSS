# 8. Random Number Generator (Generators)
# A program is needed to generate numbers for testing purposes. Create a generator
# function that produces numbers from 1 to N and prints them one by one when iterated.

# Explanation:-
# yield produces values one at a time.
# range() generates numbers from 1 to N.
# Generators save memory because they do not store all values at once.

import random

# Generate a random integer between 1 and n  (inclusive)
n = 100
random_number = random.randint(1, n)

print(f"Your random number is: {random_number}")

# Generator function
def generate_numbers(n):

    # Generate numbers from 1 to n
    for i in range(1, n + 1):
        yield i


# Call generator function
numbers = generate_numbers(5)

# Print numbers one by one
for num in numbers:
    print(num)
    break