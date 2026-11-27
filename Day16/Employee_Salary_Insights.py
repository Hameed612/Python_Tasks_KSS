# 3. Employee Salary Insights

# Scenario:
# salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
# departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Task:
# ● Convert into DataFrame
# ● Plot:
# ○ Line graph → salary trend
# ○ Bar chart → department-wise salary comparison
# ○ Pie chart → department distribution
# ○ Histogram → salary distribution
# ○ Scatter plot → index vs salary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store salary and department data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])

departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Create DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

# Display DataFrame
print(df)

# Create 5 graphs
plt.figure(figsize=(12, 8))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(df["Salary"], marker="o")
plt.title("Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")

# 2. Bar chart
plt.subplot(2, 3, 2)

# Calculate department-wise salary
dept_salary = df.groupby("Department")["Salary"].sum()

plt.bar(dept_salary.index, dept_salary.values)
plt.title("Department-wise Salary")
plt.xlabel("Department")
plt.ylabel("Total Salary")

# 3. Pie chart
plt.subplot(2, 3, 3)

dept_count = df["Department"].value_counts()

plt.pie(dept_count.values,
        labels=dept_count.index,
        autopct="%1.1f%%")
plt.title("Department Distribution")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(salaries, bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(range(len(salaries)), salaries)
plt.title("Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")

# Adjust spacing
plt.tight_layout()

# Display graphs
plt.show()