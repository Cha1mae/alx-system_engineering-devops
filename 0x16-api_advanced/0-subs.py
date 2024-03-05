#!/usr/bin/python3
"""This returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Constructing URL for subreddit's about page
    Sending GET request to retrieve subreddit info
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
