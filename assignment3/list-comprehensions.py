# Task 3: List Comprehensions Practice

import csv

# Read the CSV file
with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

# Skip header (first row) and create full names list
full_names = [f"{row[1]} {row[2]}" for row in rows[1:]]
print("All employee names:")
print(full_names)

# Filter names containing letter 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames containing 'e':")
print(names_with_e)