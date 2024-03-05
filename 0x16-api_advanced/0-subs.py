#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers (not active
users, total subscribers) for a given subreddit. If an invalid subreddit
is given, the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit. """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    hdr = {"User-Agent": "0x16.api.advanced"}
    res = requests.get(url, headers=hdr, allow_redirects=False)

    if res.status_code == 200:
        res_json = res.json()
        return res_json["data"]["subscribers"]
    else:
        return 0
