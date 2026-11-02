# Question 8: Write a Python program to find the second largest number in a list.

numbers = [10, 50, 30, 80, 40, 60]

numbers = list(set(numbers))
numbers.sort()

print("Second largest number:", numbers[-2])
