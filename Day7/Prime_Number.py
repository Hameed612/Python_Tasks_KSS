# Question: 4 Write a program to check whether a number is Prime.

# Check Prime Number

num = int(input("Enter a number: "))

# Assume number is prime
count = 0

# Check divisibility
for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

# Check Prime number
if num > 1 and count == 2:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
