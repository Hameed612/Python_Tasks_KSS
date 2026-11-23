# 1. Student List Backup (Shallow Copy)

# A teacher has a list of student marks:
# marks = [50, 60, 70, 80]

# Scenario:
# She creates a backup using assignment:
# backup = marks

# Task:
# ● Modify the first element in marks.
# ● Observe the change in backup.
# ● Explain why both lists are affected.

# Create a student marks list
marks = [50, 60, 70, 80]

# Create backup using assignment
backup = marks

# Print original and backup lists
print("Original Marks:", marks)
print("Backup Marks:", backup)

# Modify first element in original list
marks[0] = 100

# Print lists after modification
print("After Modification:")
print("Original Marks:", marks)
print("Backup Marks:", backup)