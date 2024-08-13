#!/usr/bin/python3
"""
defines a function number_of_subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
        makes a call to the reddit api and returns the number
        of subscribers in the subreddit

        Args:
            subreddit:

        Return:
            number of subscribbers
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Custom'}
    val = 0

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        val = response.json()['data']['subscribers']

    return val
