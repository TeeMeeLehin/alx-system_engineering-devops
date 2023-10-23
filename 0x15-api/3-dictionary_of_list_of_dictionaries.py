#!/usr/bin/python3
""" Python script to gather data from an API and return a json file """
import json
import requests
import sys


def gather_data():
    " function to gather data from api and return json file "
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users"
    all_user_data = {}

    users_data = requests.get(user_url).json()

    for user in users_data:
        user_id = user.get("id")
        user_name = user.get("username")

        todos_url = f"{base_url}/todos?userId={user_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        user_todo_data = [
            {
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data
        ]

        all_user_data[user_id] = user_todo_data

    json_filename = f"{user_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(all_user_data, json_file)


if __name__ == "__main__":
    gather_data()
