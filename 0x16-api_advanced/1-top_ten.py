#!/usr/bin/python3
"""10 hot ppl in reddit >:)"""
import requests


def top_ten(subreddit):
    """Titles of the first 10 hot posts in a sub-reddit."""
    base_url = "https://www.reddit.com/r/"
    url = base_url + "{}/hot.json?limit=10".format(subreddit)
    user_agent = "my_unique_application:v1"
    reddit_username = "(by /u/your_reddit_username)"
    hdr = {"User-Agent": user_agent + " " + reddit_username}
    rsp = requests.get(url, headers=hdr, allow_redirects=False)

    if rsp.status_code != 200:
        print(None)
    else:
        posts = rsp.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
