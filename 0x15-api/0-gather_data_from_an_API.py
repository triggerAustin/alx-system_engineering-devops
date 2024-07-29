#!/usr/bin/python3
"""
    this script returns employ TODO list details
    based on their id from
    a rest API
"""

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
    em_name = user_response.get('name')

    # Fetch TODOs for employee
    todos = requests.get(f'{base_url}/todos', params={'userId': em_id}).json()

    return ([em_name, todos])


def display_data(data):
    """
        display employee TODOs in specified format
    """
    name = data[0]
    todos = data[1]
    n = 0
    task = ''
    for tasks in todos:
        if tasks['completed'] is True:
            n += 1
            task += '\t' + ' ' +  tasks['title'] + '\n'
    print(f'Employee {name} is done with tasks({n}/{len(todos)}):')
    print(task, end='')


if __name__ == '__main__':
    data = get_data(argv[1])
    display_data(data)
