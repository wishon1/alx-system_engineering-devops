#!/usr/bin/python3
"""Script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress and exports it to CSV.
"""
import requests
import sys


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url_content = get(url)
    user_name = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    url_content = get(url)
    tasks = url_content.json()
    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}"\n'
                       .format(user_id, user_name, task.get('completed),
                              task.get('title')))
    
