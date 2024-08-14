#!/usr/bin/python3
"""
defines a method def top_ten(subreddit)
"""

import requests


def top_ten(subreddit):
    """
    fetches from a subreddit the top ten popular/hot posts
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "Custom"}
    params = {"limit": "10"}
    request = requests.get(url, headers=headers,
                           allow_redirects=False, params=params)

    if request.status_code == 200:
        for data in request.json().get('data').get('children'):
            print(data.get('data').get('title'))
    else:
        print('None')
