#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    api_url_usr = api + "users/" + argv[1]
    api_url_todos = api + "todos?userId=" + argv[1]

    response = requests.get(api_url_usr).json()
    todo = requests.get(api_url_todos).json()

    complete_tasks = []
    for task in todo:
        if task.get("completed") is not False:
            complete_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
          response.get("name"), len(complete_tasks), len(todo)))
    for title in complete_tasks:
        print("\t {}".format(title))
