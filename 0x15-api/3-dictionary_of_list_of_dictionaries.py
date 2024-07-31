#!/usr/bin/python3
"""
    this script returns employ TODO list details
    based on their id from
    a rest API
"""

import json
import requests
from sys import argv


def get_data():
    """
        fn gets employ todo details
        args:
            employee_id: employees id
    """
    base_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f'{base_url}/users/').json()

    # Fetch TODOs for employee
    todos = requests.get(f'{base_url}/todos').json()

    return ([user_response, todos])


def store_all_json(data):
    """
        stores all employee data in json
    """
    users = data[0]
    todos = data[1]
    employee_infor = {}
    tasks = []
    i = 1
    while i <= len(users):
        for task in todos:
            if task['userId'] == i:
                index = task['userId']
                tasks.append({
                    'username': todos[i].get('username'),
                    'task': task['title'],
                    'completed': task['completed']})
        employee_infor[index] = tasks
        i += 1

    with open('todo_all_employees' + '.json', 'w') as f:
        json.dump(employee_infor, f)


if __name__ == '__main__':
    data = get_data()
    store_all_json(data)
