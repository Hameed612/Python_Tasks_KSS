# Question:2 Write a program to check whether a given number is a Strong number. 

# Check Strong Number

num = int(input("Enter a number: "))

# Store original number
original = num

# Initialize sum
total = 0

# Calculate factorial of each digit
while num > 0:
    digit = num % 10

    fact = 1

    # Find factorial
    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact

    num = num // 10

# Check Strong number
if total == original:
    print(original, "is a Strong number")
else:
    print(original, "is not a Strong number")
