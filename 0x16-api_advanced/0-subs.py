#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
"""
import requests

def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit. """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic or 'subscribers' not in dic.get('data'):
        return 0
    return dic['data']['subscribers']
