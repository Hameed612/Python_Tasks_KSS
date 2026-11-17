# 14. Performance Tracker (Decorators)
# A software team wants to track how long functions take to execute. Create a decorator
# that measures and prints the execution time of a function.

# Explanation:
# - time.time() returns the current time.
# - The decorator records start and end times.
# - Their difference gives execution time.

# Import time module
import time

# Create decorator
def calculate_time(func):

    def wrapper():

        # Start time
        start = time.time()

        # Execute function
        func()

        # End time
        end = time.time()

        # Calculate execution time
        print("Execution Time:", end - start, "seconds")

    return wrapper


# Apply decorator
@calculate_time
def my_function():

    # Simple loop
    for i in range(1000000):
        pass


# Call function
my_function()
