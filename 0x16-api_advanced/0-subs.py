#!/usr/bin/python3
"""script to read number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ function to get number of a subreddit subscribers """
    urlsearch = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {}
    headers["User-Agent"] = "redditPirateX"
    response = requests.get(urlsearch, headers=headers)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
