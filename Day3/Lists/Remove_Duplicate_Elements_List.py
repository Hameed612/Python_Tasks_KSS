# Question 7: Write a Python program to remove duplicate elements from a list.

numbers = [10, 20, 30, 20, 40, 10, 50]

unique = []

for a in numbers:
    if a not in unique:
        unique.append(a)

print("List without duplicates:", unique)
