#!/usr/bin/python3
"""This will help us gather data from
an API and export to CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee ID>")
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

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow([user_id, user.get('name'),
                                 task.get('completed'), task.get('title')])
