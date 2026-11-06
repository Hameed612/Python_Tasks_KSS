# 4. Write a recursive function to reverse a string.

def reverse_string(s):
 if len(s) == 0:
     return s
 else:
     return reverse_string(s[1:]) + s[0]
name = input("Enter a string: ")
result = reverse_string(name)
print("Reverse string =", result)
