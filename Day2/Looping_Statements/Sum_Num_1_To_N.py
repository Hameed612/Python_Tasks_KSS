#Question3: Write a Python program to find the sum of numbers from 1 to N using a loop.

a = int(input("Enter a number: "))
total = 0
for i in range(1, a + 1):
 total = total + i
print("Sum =", total)
