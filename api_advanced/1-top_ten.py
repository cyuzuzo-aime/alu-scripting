#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """ DOCUMENTATION OF TOP TEN FN """
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/yourusername)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 302:
            print(None)
            return
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post["data"].get("title"))
    except Exception:
        print(None)
