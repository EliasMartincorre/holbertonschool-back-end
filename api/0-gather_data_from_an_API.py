#!/usr/bin/python3
""" get data from the API """
import requests
import sys

if len(sys.argv) > 1:
    employee_id = sys.argv[1]
else:
    print("Usage: command id")
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
# Count the total number of tasks and the number of done tasks
total_tasks = len(todo_data)
done_tasks = 0
done_titles = []
for task in todo_data:
    if task["completed"]:
        done_tasks += 1
        done_titles.append(task["title"])

# Print the output in the required format
a = f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):"
print(a)
for title in done_titles:
    print(f"\t {title}")
