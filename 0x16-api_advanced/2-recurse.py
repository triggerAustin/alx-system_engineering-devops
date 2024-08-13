#!/usr/bin/python3
"""
defines a method def recurse(subreddit, hot_list=[])
"""

import requests


def recurse(subreddit, hot_=[], after=None):
    """
    makes an api call to the reddit api and returns
    the list of all hot topics in the subreddit
    
    Args:
        subreddit: subreddit to get articles from
        hot_: list of hot articles
        after: control value for recursive calls
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent" : "Custom"}
    params = {"after": after}

    res = requests.get(url, headers=headers, params=params)

    if res.status_code == 200:
        data = res.json().get('data')
        data_content = data.get('children')
        for item in data_content:
            articles.append(item.get('title'))
        if data.get('after') is None:
            return articles
        return recurse(subreddit, articles, data.get('after'))
    else:
        return None
