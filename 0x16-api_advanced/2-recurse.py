#!/usr/bin/python3
"""hot subreddit articles >:)"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Thee recursive function"""
    base_url = "https://www.reddit.com/r/"
    url = "{}{}/hot.json?limit=10".format(base_url, subreddit)
    hdr = {
        "User-Agent": "my_unique_application:v1 (by /u/your_reddit_username)"
    }
    param = {"limit": 100, "after": after}
    rsp = requests.get(url, headers=hdr, params=param, allow_redirects=False)

    if rsp.status_code != 200:
        return None

    data = rsp.json().get("data")
    after = data.get("after")
    hot_list += [child.get("data").get("title")
                 for child in data.get("children")]

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
