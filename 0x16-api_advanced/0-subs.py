#!/usr/bin/python3
"""Function that queries subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Use a GET request to get the number of subscribers of the subreddit."""

    # Reddit api endpoint for getting the subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # settting a custom user agent to avoid too many errors
    user_header = {"User-Agent": "Algomerix"}

    # send a get request to the Reddit API
    response = requests.get(url, headers=user_header)

    # check if the request was unsucessful return 0
    if response.status_code == 404:
        return 0
    else:
        # convert response to json and get the data
        data = response.json().get('data')
        return data.get('suscribers')
