#!/usr/bin/python3
"""This will help us gather data from an API and export to CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee ID>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    for user in users:
        if user['id'] == user_id:
            username = user['username']
            break
    else:
        print("Error: User ID not found")
        sys.exit(1)

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_response.json()

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task['userId'] == user_id:
                taskwriter.writerow([
                    user_id,
                    username,
                    task.get('completed'),
                    task.get('title')
                ])
