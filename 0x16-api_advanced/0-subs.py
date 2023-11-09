#!/usr/bin/python3
"""script to read number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    urlsearch = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {}
    headers["User-Agent"] = "redditPirateX"
    response = requests.get(urlsearch, headers=headers)
    results = response.json().get("data")
    return results.get("subscribers")

