import time
from json import JSONDecodeError

import requests

from tweetkit.twitter.auth import TwitterAuth
from tweetkit.twitter.errors import TwitterException
from tweetkit.twitter.request import *


class TwitterClient:
    def __init__(self, auth):
        if not isinstance(auth, TwitterAuth):
            auth = TwitterAuth(**auth)
        self.auth = auth
        self._last_request = None
        self._request_wait = 2  # wait time in seconds
        self.users = UserRequest(self)
        self.tweets = TweetRequest(self)

    @property
    def headers(self):
        headers = {}
        if self.auth.type == 'bearer_token':
            bearer_token = self.auth.bearer_token
            headers.update({'Authorization': 'Bearer {}'.format(bearer_token)})
        return headers

    def request(self, url, params=None):
        if params is None:
            params = {}
        current_time = time.time()
        if (self._last_request is not None) and \
                (self._last_request + self._request_wait - current_time) > 0:
            time.sleep(self._last_request + self._request_wait - current_time)
        response = requests.request("GET", url, headers=self.headers, params=params)
        self._last_request = time.time()
        if response.status_code != 200:
            raise TwitterException(response.text, [{'code': response.status_code}])
        try:
            payload = response.json()
        except JSONDecodeError as _:
            message = 'Invalid Payload: {payload}'.format(payload=response.text)
            raise TwitterException(message, errors=[])
        if ('data' not in payload) and ('errors' in payload):
            errors = list(payload['errors'])
            first_error = errors[0] if len(errors) > 0 else {}
            error_title = first_error.get('title', 'Twitter Exception')
            error_detail = first_error.get('detail', 'Details not provided.')
            message = '{}: {}'.format(error_title, error_detail)
            raise TwitterException(message, errors)
        return payload
