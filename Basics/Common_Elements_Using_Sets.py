# 3. Perform set operations using two lists

# Create two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Convert lists into sets
set1 = set(list1)
set2 = set(list2)

# Find common elements
common = set1.intersection(set2)

# Find elements present only in first list
only_first = set1.difference(set2)

# Find all unique elements
unique = set1.union(set2)

# Print results
print("Common Elements:", common)
print("Only First List:", only_first)
print("All Unique Elements:", unique)
