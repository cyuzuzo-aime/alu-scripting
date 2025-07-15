#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""

    hdrs = {
        'User-Agent': 'python:alx_topten:v1.0 (by newuser20)'
    }
    s_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(s_url, headers=hdrs, allow_redirects=False)

    if res.status_code == 200:
        json_data = res.json()
        posts = json_data.get('data', {}).get('children', [])

        for i in range(min(10, len(posts))):
            print(posts[i].get('data', {}).get('title'))
    else:
        print(None)
