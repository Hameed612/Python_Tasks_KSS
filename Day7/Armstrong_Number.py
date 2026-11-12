# Question:1 Write a program to check whether a given number is an Armstrong number or not.

# Check Armstrong Number

num = int(input("Enter a number: "))

# Store the original number
original = num

# Count the number of digits
digits = len(str(num))

# Initialize sum
total = 0

# Calculate the sum of digits
while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

# Check Armstrong number
if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
