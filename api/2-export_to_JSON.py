#!/usr/bin/python3
""" get data from the API """
import requests
import sys
from json import dump

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
lista = []
dictionary = {}
for task in todo_data:
    un = employee_data['username']
    tc = task['completed']
    lista.append({"task": task['title'], 'completed': tc, "username": un})
dictionary[task['userId']] = lista
p = f"{todo_data[0]['userId']}.json"
with open(p, 'w') as filejson:
    dump(dictionary, filejson)
