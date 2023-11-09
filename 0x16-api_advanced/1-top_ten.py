#!/usr/bin/python3
"""script to read top 10 hot posts in a subreddit"""
import requests


def top_ten(subreddit):
    """function to print top 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {}
    headers["User-Agent"] = "redditPirateX"
    p = {"limit": 10}
    response = requests.get(url, headers=headers, params=p,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
    else:
        results = (response.json().get("data").get("children"))
        for post in results:
            print(post.get("data").get("title"))
