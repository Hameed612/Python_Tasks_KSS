# 8. Write a program to check whether a string is a palindrome.

str1 = input("Enter a string: ")

if str1 == str1[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
