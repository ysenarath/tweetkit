"""Request"""
import requests

from tweetkit.exceptions import ProblemOrError, TwitterRequestException
from tweetkit.models.paginator import Paginator
from tweetkit.models.response import TwitterResponse, TwitterStreamResponse

__all__ = [
    'TwitterRequest',
]


class TwitterRequest(object):
    """Request."""

    def __init__(self, url, method='get', query=None, params=None, data=None, stream=False, auth=None, **kwargs):
        self.url = url
        self.method = method.upper()
        self.data = data
        self.query = query
        self.params = params
        self.stream = stream
        self.auth = auth
        self.kwargs = kwargs

    def send(self, paginate=False):
        """send"""
        if paginate:
            return Paginator(self)
        url = self.url.format(**self.params)
        query = {k: ','.join(v) if isinstance(v, list) else v for k, v in self.query.items()}
        r = requests.request(
            method=self.method, url=url,
            params=query, json=self.data,
            stream=self.stream, auth=self.auth
        )
        content_type = r.headers.get('content-type')
        if 200 <= r.status_code < 300:
            # The request has succeeded.
            content_types = 'application/json'
            if content_type is None and self.stream:
                return TwitterStreamResponse(r, **self.kwargs)
            elif content_type is not None and content_type.startswith(content_types):
                return TwitterResponse(r, **self.kwargs)
        else:
            error = None
            content_types = ('application/json', 'application/problem+json')
            if content_type is not None and content_type.startswith(content_types):
                # The request has failed.
                error = ProblemOrError(r)
            if error is not None:
                raise error
        raise TwitterRequestException(r)
