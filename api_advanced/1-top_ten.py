#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit."""

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
