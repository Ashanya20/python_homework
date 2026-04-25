import pandas as pd
import json

# Task 1: Creating and Manipulating DataFrames

# Create DataFrame from dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
task1_data_frame = pd.DataFrame(data)
print("\nTask 1\nDataFrame:\n", task1_data_frame)

# Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print("\nWith Salary:\n", task1_with_salary)

# Modify an existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print("\nAges incremented:\n", task1_older)

# Save the DataFrame as a CSV file
task1_older.to_csv("employees.csv", index=False)
print("\nSaved to employees.csv")


# Task 2: Loading Data from CSV and JSON

# Read CSV file
task2_employees = pd.read_csv("employees.csv")
print("\nTask 2\nCSV data:\n", task2_employees)

# Read data from a JSON file
additional_data = {
    "Name": ["Eve", "Frank"],
    "Age": [28, 40],
    "City": ["Miami", "Seattle"],
    "Salary": [60000, 95000]
}
with open("additional_employees.json", "w") as file:
    json.dump(additional_data, file)

json_employees = pd.read_json("additional_employees.json")
print("\nJSON data:\n", json_employees)

# Combine DataFrames (concatenate rows)
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nCombined DataFrame:\n", more_employees)

# Task 3: Data Inspection

# First 3 rows
first_three = more_employees.head(3)
print("\nTask 3\nFirst 3 rows:\n", first_three)

# Last 2 rows
last_two = more_employees.tail(2)
print("\nLast 2 rows:\n", last_two)

# Shape
employee_shape = more_employees.shape
print("\nShape of DataFrame:", employee_shape)

# Info
print("\nDataFrame info:")
more_employees.info()

# Task 4: Data Cleaning

# 1. Load dirty data
dirty_data = pd.read_csv("dirty_data.csv")
print("\nTask 4\nOriginal dirty data:\n", dirty_data)

# Create a copy
clean_data = dirty_data.copy()

# 2. Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("\nWithout duplicates:\n", clean_data)

# 3. Convert Age to numeric
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\nAge to numeric:\n", clean_data)

# 4. Convert Salary to numeric
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\nSalary to numeric:\n", clean_data)

# 5. Fill missing numeric values
age_mean = clean_data["Age"].mean()
salary_median = clean_data["Salary"].median()
clean_data["Age"] = clean_data["Age"].fillna(age_mean)
clean_data["Salary"] = clean_data["Salary"].fillna(salary_median)
print("\nFilling missing values:\n", clean_data)

# 6. Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(pd.Timestamp("1900-01-01"))
print("\nHire Date to datetime:\n", clean_data)

# 7. Strip whitespace and standardize Name and Department as uppercase
if "Name" in clean_data.columns:
    clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
if "Department" in clean_data.columns:
    clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print("\nCleaning Name and Department:\n", clean_data)
