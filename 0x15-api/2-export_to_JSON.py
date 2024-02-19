#!/usr/bin/python3
"""Exports data to JSON format"""

from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':
    # Get user ID from command-line arguments
    user_id = argv[1]

    # Fetch user data from the API
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = get(user_url)
    username = user_response.json().get('username')

    # Fetch user's tasks from the API
    tasks_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                 user_id)
    tasks_response = get(tasks_url)
    tasks = tasks_response.json()

    # Create a dictionary to store user's tasks
    user_tasks = {user_id: []}

    # Iterate over each task and store it in the dictionary
    for task in tasks:
        user_tasks[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    # Write the dictionary to a JSON file
    with open('{}.json'.format(user_id), 'w') as file:
        dump(user_tasks, file)
