#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a
       given subreddit.
    """
    # Construct the URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Set custom headers including User-Agen to avoid too many error
    headers = {"User-Agent": "My User Agent 1.0"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is not found or private
    if response.status_code == 404:
        print("None")
        return
    else:
        # Get the JSON response data
        data = response.json().get("data")

        # Extract the list of post objects from the response data
        children = data.get("children")

        # Print the titles of the top 10 posts
        for post in range(10):
            title = children[post].get("data").get("title")
            print(title)
