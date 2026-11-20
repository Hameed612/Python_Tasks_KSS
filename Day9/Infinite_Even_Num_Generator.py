# 15. Infinite Even Number Generator (Generators)
# Create a generator function that continuously generates even numbers starting from
# 2. The program should print the first N even numbers using this generator.

# Explanation:
# - while True creates an infinite loop.
# - yield generates one value at a time.
# - next() gets the next generated number.
# - num += 2 generates even numbers.

# Create infinite generator
def even_numbers():

    num = 2

    # Generate even numbers continuously
    while True:
        yield num
        num += 2


# Create generator object
numbers = even_numbers()

# Number of values to print
n = 10

# Print first 10 even numbers
for i in range(n):
    print(next(numbers))