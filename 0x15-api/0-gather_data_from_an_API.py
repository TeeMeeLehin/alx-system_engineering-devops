#!/usr/bin/python3
""" Python script to gather data from an API """
import requests
import sys


def gather_data(user_id: int):
    " function to gather data from api "
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{user_id}"
    todos_url = f"{base_url}/todos?userId={user_id}"

    user_data = requests.get(user_url).json()
    name = user_data.get("name")

    todos_data = requests.get(todos_url).json()
    num_todos = len(todos_data)
    compltd_tasks = [task for task in todos_data if task.get("completed")]
    num_compltd = len(compltd_tasks)

    print(f"Employee {name} is done with tasks ({num_compltd}/{num_todos}):")

    for task in compltd_tasks:
        print(f"\t{task.get('title')}")

    return


if __name__ == "__main__":
    usr_id = int(sys.argv[1])
    gather_data(usr_id)
