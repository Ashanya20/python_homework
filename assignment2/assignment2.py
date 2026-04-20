import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2: Read a CSV File
def read_employees():
    try:
        employees_dict = {}
        rows_list = []
        
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    employees_dict["fields"] = row
                else:
                    rows_list.append(row)
        
        employees_dict["rows"] = rows_list
        return employees_dict
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        return {}

employees = read_employees()
# print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    col_idx = column_index("first_name")
    return employees["rows"][row_number][col_idx]
# print(first_name(0))

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches
# print(employee_find(11))

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches
# print(employee_find_2(10))

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_idx])
    return employees["rows"]

# Task 8: Create a dict for an Employee
def employee_dict(row):
    emp_id_idx = column_index("employee_id")
    result = {}
    for i in range(len(employees["fields"])):
        if i != emp_id_idx:
            result[employees["fields"][i]] = row[i]
    return result

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    emp_id_idx = column_index("employee_id")
    result = {}
    for row in employees["rows"]:
        emp_id = row[emp_id_idx]
        result[emp_id] = employee_dict(row)
    return result
# print(all_employees_dict())

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")
# print(get_this_value())

# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("another_secret")
# print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_csv_to_dict(filepath):
    result = {}
    rows_list = []
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                result["fields"] = row
            else:
                rows_list.append(tuple(row))  # Convert row to tuple
    result["rows"] = rows_list
    return result

def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
# print("minutes1:", minutes1)
# print("minutes2:", minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)
minutes_set = create_minutes_set()
# print("minutes_set:", minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return converted
minutes_list = create_minutes_list()
# print("minutes_list:", minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    
    return converted
sorted_output = write_sorted_list()
# print("Sorted output:", sorted_output)