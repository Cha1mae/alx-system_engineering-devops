#!/usr/bin/python3
"""hot articles again"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after="", words_counts=Counter()):
    """th e recrusive function"""
    base_url = "https://www.reddit.com/r/"
    url = "{}{}/hot.json".format(base_url, subreddit)
    hdr = {
        "User-Agent": "my_unique_application:v1 (by /u/your_reddit_username)"
    }
    param = {"limit": 100, "after": after}
    rsp = requests.get(url, headers=hdr, params=param, allow_redirects=False)

    if rsp.status_code != 200:
        return

    data = rsp.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title").lower()
        words = title.split()
        for word in words:
            if word in word_list:
                words_counts[word] += 1

    if after is not None:
        count_words(subreddit, word_list, after, words_counts)
    else:
        words_counts = {b: d for b, d in sorted(
            words_counts.items(), key=lambda item: (-item[1], item[0]))}
        for word, count in words_counts.items():
            print("{}: {}".format(word, count))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(sys.argv[1], word_list)
