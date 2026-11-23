# 11. Boolean Masking for Salary Analysis

# Scenario:
# Employee salaries: [25000, 40000, 15000, 50000, 30000]

# Task:
# ● Filter salaries above 30000.
# ● Count how many employees satisfy this condition.

# Import NumPy
import numpy as np

# Store employee salaries
salary = np.array([25000, 40000, 15000, 50000, 30000])

# Filter salaries above 30000
result = salary[salary > 30000]

# Count filtered employees
count = len(result)

# Print results
print("Salaries Above 30000:", result)
print("Number of Employees:", count)