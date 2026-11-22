# 9. Reshaping Sales Data

# A company stores monthly sales data:
# sales_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# Scenario:
# You need to display the data as 4 months × 3 products matrix.

# Task:
# ● Convert the list to NumPy array.
# ● Reshape it into a 4 × 3 array.

# Import NumPy
import numpy as np

# Store monthly sales
sales = [10, 20, 30, 40, 50, 60,
         70, 80, 90, 100, 110, 120]

# Convert into NumPy array
arr = np.array(sales)

# Reshape into 4 rows and 3 columns
new_arr = arr.reshape(4, 3)

# Print reshaped array
print("Sales Matrix:")
print(new_arr)