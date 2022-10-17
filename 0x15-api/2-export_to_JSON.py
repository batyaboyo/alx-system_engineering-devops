#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    api_url_usr = api + "users/" + argv[1]
    api_url_todos = api + "todos?userId=" + argv[1]

    response = requests.get(api_url_usr).json()
    todo = requests.get(api_url_todos).json()

    filename = argv[1] + ".json"

    content = {argv[1]: []}
    for task in todo:
        content[argv[1]].append({"task": task.get("title"),
                                "completed": task.get("completed"),
                                 "username": response.get("username")})
    content = json.dumps(content)
    with open(filename, 'w', newline='') as jsonfile:
        jsonfile.write(content)
