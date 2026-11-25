# 2. Missing City Data (NaN Handling)

# A dataset contains city populations:
# cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}

# Scenario:
# You want data for:
# ["Delhi", "Chennai", "Bangalore"]

# Task:
# ● Create a Series with the above index
# ● Identify which cities have missing values (NaN)

# Import pandas
import pandas as pd

# Create dictionary
cities = {
    "Delhi": 2000000,
    "Mumbai": 3000000,
    "Chennai": 1500000
}

# Create Series with required city names
S = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

# Display Series
print("City Population:")
print(S)

# Check missing values
print("Missing Values:")
print(S.isna())

# Display cities having missing values
print("Cities with Missing Data:")
print(S[S.isna()])