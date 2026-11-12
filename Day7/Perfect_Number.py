# Question:5 Write a program to check whether a number is a Perfect number.

# Check Perfect Number

num = int(input("Enter a number: "))

# Initialize sum
total = 0

# Find proper divisors
for i in range(1, num):
    if num % i == 0:
        total = total + i

# Check Perfect number
if num > 0 and total == num:
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")
