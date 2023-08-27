#!/usr/bin/python3
""" get data from the API """
import requests
from json import dump


# Get the employee data from the API
employee_url = f"https://jsonplaceholder.typicode.com/users/"
employee_response = requests.get(employee_url)
employee_data = employee_response.json()

dictionary = {}
for usuario in employee_data:
    lista = []
    url = f"https://jsonplaceholder.typicode.com/todos?userId={usuario['id']}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    for task in todo_data:
        t = task['title']
        s = task['completed']
        un = usuario['username']
        lista.append({"username": un, "task": t, 'completed': s})

    dictionary[task['userId']] = lista
with open('todo_all_employees.json', 'w') as filejson:
    dump(dictionary, filejson)
