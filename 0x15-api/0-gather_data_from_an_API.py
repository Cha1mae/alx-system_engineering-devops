#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    if user_response.status_code != 200:
        print("Error: User ID not found")
        sys.exit(1)

    user = user_response.json()

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODOs")
        sys.exit(1)

    todos = todos_response.json()

    done_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)

    print(f"Employee {user.get('name')} is done with tasks"
          f"({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print("\t", task.get('title'))
