# 5. Nested Data Independence (Deep Copy)

# A school stores classroom data:
# classes = [["Math", [30, 35]], ["Science", [25, 28]]]

# Scenario:
# ● Create a deep copy of this structure.
# ● Modify student count in original.

# Task:
# ● Prove that copied data remains unchanged.
# ● Explain why deep copy is required here.

# Import copy module
import copy

# Create classroom data
classes = [["Math", [30, 35]],
           ["Science", [25, 28]]]

# Create deep copy
backup = copy.deepcopy(classes)

# Modify original student count
classes[0][1][0] = 50

# Print original data
print("Original Data:", classes)

# Print copied data
print("Backup Data:", backup)