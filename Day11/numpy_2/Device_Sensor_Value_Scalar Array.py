# 2. Device Sensor Value (Scalar Array)

# An IoT device records a single sensor reading = 75.

# Task:
# ● Create a 0-D NumPy array with this value.
# ● Print the value and check its number of dimensions.

# Import NumPy
import numpy as np

# Create a 0-D array
sensor = np.array(75)

# Print sensor value
print("Sensor Value:", sensor)

# Print number of dimensions
print("Dimensions:", sensor.ndim)