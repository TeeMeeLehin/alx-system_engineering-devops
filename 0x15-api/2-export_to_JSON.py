#!/usr/bin/python3
""" Python script to gather data from an API and return a json file """
import json
import requests
import sys


def gather_data(user_id: int):
    " function to gather data from api and return json file "
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{user_id}"
    todos_url = f"{base_url}/todos?userId={user_id}"

    user_data = requests.get(user_url).json()
    uid = user_data.get("id")
    name = user_data.get("username")

    todos_data = requests.get(todos_url).json()

    json_data = {
        uid: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": name
            }
            for task in todos_data
        ]
    }

    json_filename = f"{uid}.json"
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    usr_id = int(sys.argv[1])
    gather_data(usr_id)
