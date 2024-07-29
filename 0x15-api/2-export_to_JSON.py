#!/usr/bin/python3
"""
    this script returns employ TODO list details
    based on their id from
    a rest API
"""
import json
import requests
from sys import argv


def get_data(em_id):
    """
        fn gets employ todo details
        args:
            employee_id: employees id
    """
    base_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f'{base_url}/users/{em_id}').json()

    # Fetch TODOs for employee
    todos = requests.get(f'{base_url}/todos', params={'userId': em_id}).json()

    return ([user_response, todos])


def store_json(data):
    """
        stores employee details in json
        args:
            data: returned from API call
    """
    name = data[0].get('username')
    user_infor = {}
    tasks = []
    for task in data[1]:
        tasks.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': name})
    user_infor[task['userId']] = tasks
    with open(str(argv[1]) + '.json', mode='w') as f:
        json.dump(user_infor, f)


if __name__ == '__main__':
    data = get_data(argv[1])
    store_json(data)
