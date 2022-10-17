"""Twitter API v2"""
from tweetkit.models import TwitterRequest
from tweetkit.requests import Bookmarks, Compliance, General, Lists, Spaces, Tweets, Users


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

    def request(self, url, method='get', query=None, params=None, data=None, stream=False, paginate=False,
                **kwargs):
        """make request and get response."""
        url = '{}/{}'.format(self.url, url.lstrip('/'))
        request = TwitterRequest(
            url, method=method, query=query, params=params, data=data,
            stream=stream, auth=self.auth, **kwargs
        )
        return request.send(paginate=paginate)
