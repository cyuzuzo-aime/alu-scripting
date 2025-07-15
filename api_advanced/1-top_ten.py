#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: If the subreddit is invalid or an error occurs.
    """
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid Too Many Requests errors.
    # Reddit's API requires a User-Agent.
    headers = {
        "User-Agent": "my_reddit_api_script/1.0 (by /u/your_reddit_username)"
    }

    try:
        # Make the GET request to the Reddit API.
        # allow_redirects=False is crucial to handle invalid subreddits
        # that might redirect to search results.
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Extract the list of posts from the JSON response
            posts = data.get('data', {}).get('children', [])

            # Print the titles of the first 10 hot posts
            for i, post in enumerate(posts):
                if i >= 10:
                    break # Stop after printing 10 titles
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
        else:
            # If status code is not 200 (e.g., 404 Not Found, or 3xx redirect),
            # it means the subreddit is likely invalid or an issue occurred.
            print(None)

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., no internet connection, DNS failure)
        print(None)
        # Optionally, print the error for debugging purposes:
        # print(f"An error occurred: {e}", file=sys.stderr)

    except ValueError:
        # Handle JSON decoding errors (e.g., if the response is not valid JSON)
        print(None)
        # Optionally, print the error for debugging purposes:
        # print(f"Failed to decode JSON response.", file=sys.stderr)
