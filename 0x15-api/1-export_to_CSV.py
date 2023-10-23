#!/usr/bin/python3
""" Python script to gather data from an API and return a csv file """
import csv
import requests
import sys


def gather_data(user_id: int):
    " function to gather data from api and return csv file "
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{user_id}"
    todos_url = f"{base_url}/todos?userId={user_id}"

    user_data = requests.get(user_url).json()
    uid = user_data.get("id")
    name = user_data.get("username")

    todos_data = requests.get(todos_url).json()

    csv_filename = f"{uid}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        for task in todos_data:
            title = task.get("title")
            stat = task.get("completed")
            csv_writer.writerow([uid, name, stat, title])


if __name__ == "__main__":
    usr_id = int(sys.argv[1])
    gather_data(usr_id)
