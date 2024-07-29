#!/usr/bin/python3
"""
    this script returns employ TODO list details
    based on their id from
    a rest API and writes data into csv file
"""

import csv
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


def store_csv(data):
    """
        stores employee data in csv
    """
    n = 0
    name = data[0].get('name').split(' ')
    csv_filename = f'{argv[1]}.csv'
    with open(csv_filename, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in data[1]:
            writer.writerow([argv[1], name[0], task['completed'],
                            task['title']])


if __name__ == '__main__':
    data = get_data(argv[1])
    store_csv(data)
