#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    api_url_usr = api + "users/"
    api_url_todos = api + "todos/"

    response = requests.get(api_url_usr).json()
    todo = requests.get(api_url_todos).json()

    filename = "todo_all_employees.json"

    content = {}

    for user in response:
        id = user.get("id")
        content[id] = []
        for task in todo:
            if task.get("userId") == id:
                content[id].append({"username": user.get("username"),
                                    "task": task.get("title"),
                                    "completed": task.get("completed")})
    content = json.dumps(content)
    with open(filename, 'w') as jsonfile:
        jsonfile.write(content)
