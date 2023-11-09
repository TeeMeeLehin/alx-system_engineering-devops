#!/usr/bin/python3
"""script to read top 10 hot posts in a subreddit"""
import requests


def top_ten(subreddit):
    """function to print top 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {}
    headers["User-Agent"] = "redditPirateX"
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print("None")
    else:
        results = (response.json().get("data").get("children"))
        for i in range(10):
            print(results[i].get("data").get("title"))
