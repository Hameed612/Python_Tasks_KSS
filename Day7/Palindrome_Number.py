# Question 3 : Write a program to check whether a number is a Palindrome.

# Check Palindrome Number

num = int(input("Enter a number: "))

# Store original number
original = num

# Initialize reverse
reverse = 0

# Reverse the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check Palindrome
if original == reverse:
    print(original, "is a Palindrome number")
else:
    print(original, "is not a Palindrome number")
