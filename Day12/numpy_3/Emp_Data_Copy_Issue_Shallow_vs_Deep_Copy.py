# 3. Employee Data Copy Issue (Shallow vs Deep Copy)

# A company stores employee data:
# employees = [[101, "A"], [102, "B"], [103, "C"]]

# Scenario:
# ● Create a shallow copy of the list.
# ● Modify one nested list (e.g., change "A" to "Z").
# ● Observe changes in both lists.

# Task:
# ● Explain why the change reflects in both.
# ● Fix it using deep copy.

# Import copy module
import copy

# Create employee data
employees = [[101, "A"], [102, "B"], [103, "C"]]

# Create shallow copy
shallow = copy.copy(employees)

# Modify nested list
employees[0][1] = "Z"

# Print both lists
print("Original:", employees)
print("Shallow Copy:", shallow)

# Create deep copy
deep = copy.deepcopy(employees)

# Modify original list again
employees[0][1] = "X"

# Print original and deep copy
print("After Modification:")
print("Original:", employees)
print("Deep Copy:", deep)