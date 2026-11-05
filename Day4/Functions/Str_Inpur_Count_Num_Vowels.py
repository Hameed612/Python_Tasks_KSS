# 9. Write a function that takes a string as input and returns the number of vowels.

def vowels(str1):
    count = 0

    for ch in str1:
        if ch.lower() in "aeiou":
            count = count + 1

    return count

s = input("Enter a string: ")

print("Number of vowels:", vowels(s))
