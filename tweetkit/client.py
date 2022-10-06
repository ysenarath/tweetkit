"""Twitter API v2"""
from __future__ import absolute_import

import requests

from tweetkit.operations import Bookmarks, Compliance, General, Lists, Spaces, Tweets, Users


class TwitterClient(object):
    """Twitter API Client.

    Twitter API v2 available endpoints.

    Notes
    -----
    Please refer to the following for more information on using the Twitter API.
        - Twitter Developers: `https://developer.twitter.com<https://developer.twitter.com>`__.
        - Twitter Developer Agreement and Policy: `https://developer.twitter.com/en/developer-terms/agreement-and-policy.html<https://developer.twitter.com/en/developer-terms/agreement-and-policy.html>`__.
    """

    url = 'https://api.twitter.com'
    version = '2.51'

    def __init__(self, auth):
        self.auth = auth
        self.bookmarks = Bookmarks(self)
        self.compliance = Compliance(self)
        self.general = General(self)
        self.lists = Lists(self)
        self.spaces = Spaces(self)
        self.tweets = Tweets(self)
        self.users = Users(self)

    def request(self, path, method='get', query=None, params=None, data=None, stream=False):
        """Create a request object and return.

        Parameters
        ----------
        path: str
        method: str
        query: dict, optional
        params: dict, optional
        data: dict, optional
        stream: bool, optional

        Returns
        -------
        request: Request
            Request object.
        """
        formatted_path = path.format(**params)
        url = '{}/{}'.format(self.url.rstrip('/'), formatted_path.lstrip('/'))
        r = requests.request(method.upper(), url, params=query, json=data, stream=stream, auth=self.auth)
        return r
