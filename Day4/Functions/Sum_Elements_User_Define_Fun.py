# 8. Write a function to find the sum of elements in a list using a user-defined function.

def total(numbers):
    sum1 = 0

    for i in numbers:
        sum1 = sum1 + i

    return sum1

a = [10, 20, 30, 40, 50, 60]

print("Sum of list:", total(a))
