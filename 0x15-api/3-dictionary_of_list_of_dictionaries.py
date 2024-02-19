#!/usr/bin/python3
"""This will ather all data from an API and export it to JSON"""

import json
import requests

if __name__ == "__main__":
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    if users_response.status_code != 200:
        print("Error: Unable to fetch users")
        sys.exit(1)

    users = users_response.json()
    all_tasks = {}

    for user in users:
        user_id = user.get('id')
        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
        if todos_response.status_code != 200:
            print(f"Error: Unable to fetch TODOs for user {user_id}")
            continue

        todos = todos_response.json()

        tasks = []
        for task in todos:
            tasks.append({
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        all_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
