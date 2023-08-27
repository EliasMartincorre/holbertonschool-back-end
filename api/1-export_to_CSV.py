#!/usr/bin/python3
""" get data from the API """
import requests
import sys
import csv

if len(sys.argv) > 1:
    employee_id = sys.argv[1]
else:
    print("usage: comand + id")
    exit()


# Get the employee data from the API
employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
employee_response = requests.get(employee_url)
employee_data = employee_response.json()

# Get the employee name from the data
employee_name = employee_data["name"]

# Get the  list data from the API
todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
todo_response = requests.get(todo_url)
todo_data = todo_response.json()

with open(f"{sys.argv[1]}.csv", 'w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for task in todo_data:
        n = employee_data['username']
        writer.writerow([task['userId'], n, task['completed'], task['title']])
