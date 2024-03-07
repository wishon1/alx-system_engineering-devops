#!/usr/bin/python3
"""Function that queries subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Use a GET request to get the number of subscribers of the subreddit."""

    # Reddit api endpoint for getting the subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # settting a custom user agent to avoid too many errors
    user_header = {"User-Agent": "My user Agent 1.0"}

    # send a get request to the Reddit API and convert response to json
    response = requests.get(url, headers=user_header).json()

    # check if the request was unsucessful return 0
    try:
        return response.get('data').get('suscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
