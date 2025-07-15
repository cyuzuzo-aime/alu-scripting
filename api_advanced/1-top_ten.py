#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "scripting/1.0 (by /u/user0221)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for i, post in enumerate(posts):
                if i >= 10:
                    break
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
        else:
            print(None)

    except requests.exceptions.RequestException as e:
        print(None)

    except ValueError:
        print(None)
