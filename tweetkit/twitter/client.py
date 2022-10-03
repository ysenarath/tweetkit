"""Twitter API v2"""

from tweetkit.twitter.requests import Bookmarks, Compliance, General, Lists, Spaces, Tweets, Users


class Request(object):
    """Request"""

    def __init__(self, url):
        """Initialize a new request object.

        Parameters
        ----------
        url: str
            The base url to use for sending new requests.
        """
        self.url = url

    def __call__(self, path, method='get', query=None, params=None, data=None):
        """Send the request.

        Parameters
        ----------
        path: str
        method: str
        query: dict, optional
        params: dict, optional

        Returns
        -------

        """
        pass


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

    def __init__(self):
        self.bookmarks = Bookmarks(self)
        self.compliance = Compliance(self)
        self.general = General(self)
        self.lists = Lists(self)
        self.spaces = Spaces(self)
        self.tweets = Tweets(self)
        self.users = Users(self)

    @property
    def request(self):
        """Create a request object and return.

        Parameters
        ----------


        Returns
        -------
        request: Request
            Request object.
        """
        return Request(url=self.url)
