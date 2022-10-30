"""Request"""
import collections
import datetime
import time

import requests

from tweetkit.exceptions import ProblemOrError, TwitterRequestException
from tweetkit.models.paginator import Paginator
from tweetkit.models.response import TwitterResponse, TwitterStreamResponse

__all__ = [
    'TwitterRequest',
]


class TwitterRequestScheduler(object):
    """TwitterRequestScheduler"""

    def __init__(self):
        # for more see: https://developer.twitter.com/en/docs/twitter-api/rate-limits
        # how to calculate: <number of requests> / (<request limit interval in minutes (usually 15)> * 60),
        self.rate_limit = 1.0
        self.last_request_time = None
        self.rate_limit_remaining = None
        self.rate_limit_reset = None

    @property
    def min_max_rate_limit(self):
        """Calculates minimum of maximum rate limit from the rate limit parameter.

        This is required when multiple values are provided.

        Returns
        -------
        Minimum of maximum rate limit (i.e., this will result in maximum wait period).
        """
        if isinstance(self.rate_limit, collections.Sequence) and not isinstance(self.rate_limit, str):
            rate_limit = min(self.rate_limit)
        else:
            rate_limit = self.rate_limit
        return rate_limit

    @property
    def min_wait_period(self):
        """Calculates minimum wait period in between two requests."""
        return 1 / self.min_max_rate_limit

    def wait(self):
        """wait"""
        # manage rate limiting
        if self.last_request_time is not None:
            current_time = datetime.datetime.now()
            elapsed_time = (current_time - self.last_request_time).total_seconds()
            if elapsed_time < self.min_wait_period:
                time.sleep(self.min_wait_period - elapsed_time)

    def update(self, r=None):
        """update"""
        # update the latest request time to current time on update
        self.last_request_time = datetime.datetime.now()
        if r is None:
            # nothing else to do
            return self
        x_rate_limit_limit = None
        try:
            # the rate limit ceiling for that given endpoint
            x_rate_limit_limit = float(r.headers.get('x-rate-limit-limit'))
        except TypeError as ex:
            # keep current rate limit
            pass
        finally:
            if x_rate_limit_limit is not None:
                self.rate_limit = float(x_rate_limit_limit) / (15 * 60)
        x_rate_limit_remaining = None
        try:
            # the number of requests left for the 15-minute window
            x_rate_limit_remaining = int(r.headers.get('x-rate-limit-remaining'))
        except TypeError as ex:
            # rate limit remaining is unknown
            pass
        self.rate_limit_remaining = x_rate_limit_remaining
        x_rate_limit_reset = None
        try:
            # the remaining window before the rate limit resets, in UTC epoch seconds
            x_rate_limit_reset = int(r.headers.get('x-rate-limit-reset'))
        except TypeError as ex:
            pass  # rate limit remaining is unknown
        self.rate_limit_reset = x_rate_limit_reset
        return self

    def __repr__(self):
        return 'TwitterRequestScheduler(rate_limit={:0.2f}, last_request_time=\'{}\', rate_limit_remaining={:d}, rate_limit_reset={:d})'.format(
            self.rate_limit,
            self.last_request_time,
            self.rate_limit_remaining,
            self.rate_limit_reset,
        )


class TwitterRequest(object):
    """Request."""

    def __init__(self, url, method='get', query=None, params=None, data=None, stream=False, auth=None, scheduler=None,
                 **kwargs):
        self.url = url
        self.method = method.upper()
        self.data = data
        self.query = query
        self.params = params
        self.stream = stream
        self.auth = auth
        if scheduler is None:
            scheduler = TwitterRequestScheduler()
        self.scheduler = scheduler
        self.kwargs = kwargs
        # timer

    def send(self, paginate=False):
        """send"""
        if paginate:
            return Paginator(self)
        url = self.url.format(**self.params)
        query = {k: ','.join(v) if isinstance(v, list) else v for k, v in self.query.items()}
        # wait before request
        self.scheduler.wait()
        r = requests.request(
            method=self.method, url=url,
            params=query, json=self.data,
            stream=self.stream, auth=self.auth
        )
        # update after request
        self.scheduler.update(r)
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
