#!/usr/bin/python3
"""this will gather data from an API and export it to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee ID>")
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

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    with open(f'{user_id}.json', 'w') as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
