# 7. Generator-based Log Reader

# Scenario:
# A large log file needs to be processed.

# Task:
# ● Create a generator to read file line by line
# ● Use loop to process logs
# ● Use condition to filter errors
# ● Count occurrences using a dictionary


# Generator-based Log Reader

# Create sample log file
with open("logs.txt", "w") as file:
    file.write("INFO Login successful\n")
    file.write("ERROR File not found\n")
    file.write("INFO User logged out\n")
    file.write("ERROR Connection failed\n")

# Generator function
def read_logs():

    with open("logs.txt", "r") as file:

        for line in file:
            yield line.strip()

# Dictionary to count logs
count = {}

# Read and process logs
for log in read_logs():

    print(log)

    # Check error messages
    if "ERROR" in log:

        if "ERROR" in count:
            count["ERROR"] += 1
        else:
            count["ERROR"] = 1

print("\nError Count:", count)
