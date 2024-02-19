#!/usr/bin/python3
"""Exports data in JSON format"""

from json import dump
from requests import get


if __name__ == '__main__':
    # URL for fetching user data
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    # Fetch user data from the API
    users_response = get(users_url)
    # Extract user information
    users = users_response.json()

    # Dictionary to store user tasks
    user_tasks_dict = {}

    # Iterate over each user
    for user in users:
        # Get user ID and username
        user_id = user.get('id')
        username = user.get('username')

        # URL for fetching user's tasks
        user_tasks_url = (
            'https://jsonplaceholder.typicode.com/users/{}/todos/'
            .format(user_id)
        )
        # Fetch user's tasks from the API
        user_tasks_response = get(user_tasks_url)

        # Extract user's tasks
        tasks = user_tasks_response.json()

        # Initialize task list for the user
        user_tasks_dict[user_id] = []

        # Iterate over each task of the user
        for task in tasks:
            # Add task details to the user's task list
            user_tasks_dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    # Write the dictionary containing all user tasks to a JSON file
    with open('todo_all_employees.json', 'w') as file:
        dump(user_tasks_dict, file)
