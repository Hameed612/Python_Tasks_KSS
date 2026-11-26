# 9. Smart Data Processing Pipeline

# Scenario:
# A system processes numeric data from file.

# Task:
# ● Read numbers from a file
# ● Use NumPy for calculations (mean, std)
# ● Convert results to Pandas DataFrame
# ● Use exception handling for bad data
# ● Use a generator to stream data
# ● Apply decorator to measure execution time


# Smart Data Processing Pipeline

import numpy as np
import pandas as pd
import time

# Create sample file
with open("numbers.txt", "w") as file:
    file.write("10\n20\n30\n40\n50\n")

# Generator to read numbers
def read_numbers():

    with open("numbers.txt", "r") as file:

        for line in file:
            yield line.strip()


# Decorator to calculate execution time
def timer(function):

    def wrapper():

        start = time.time()

        function()

        end = time.time()

        print("Execution Time:", end - start)

    return wrapper


# Apply decorator
@timer
def process_data():

    numbers = []

    # Read numbers from file
    for value in read_numbers():

        try:
            numbers.append(float(value))

        except ValueError:
            print("Invalid data:", value)

    # Convert into NumPy array
    arr = np.array(numbers)

    if len(arr) > 0:

        # Calculate mean and standard deviation
        mean = np.mean(arr)
        std = np.std(arr)

        # Create DataFrame
        data = pd.DataFrame({
            "Mean": [mean],
            "Standard Deviation": [std]
        })

        print(data)

    else:
        print("No valid numbers found")


# Run program
process_data()
