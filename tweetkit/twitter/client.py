import json
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
        self.stream = TweetStreamRequest(self)
        self.response = None

    @property
    def headers(self):
        headers = {}
        if self.auth.type == 'bearer_token':
            bearer_token = self.auth.bearer_token
            headers.update({'Authorization': 'Bearer {}'.format(bearer_token)})
        return headers

    def stream_response(self, response):
        def _generator():
            for response_line in response.iter_lines():
                payload_data = None
                if response_line:
                    payload_data = json.loads(response_line)
                self.response = payload_data
                yield payload_data

        return _generator

    def request(self, url, params=None, method='GET', data=None, stream=False):
        if data is None:
            data = {}
        if params is None:
            params = {}
        current_time = time.time()
        if (self._last_request is not None) and \
                (self._last_request + self._request_wait - current_time) > 0:
            time.sleep(self._last_request + self._request_wait - current_time)
        if method.upper() == 'GET':
            response = requests.request('GET', url, headers=self.headers, params=params, stream=stream)
        elif method.upper() == 'POST':
            response = requests.request('POST', url, headers=self.headers, params=params, json=data, stream=stream)
        else:
            raise ValueError('Invalid method type. Found {}, Expected one of \'GET\' or \'POST\''.format(str(method)))
        self._last_request = time.time()
        if 200 <= response.status_code < 300:
            try:
                payload = response.json()
                if 'errors' in payload:
                    errors = list(payload['errors'])
                    first_error = errors[0] if len(errors) > 0 else {}
                    error_title = first_error.get('title', 'Twitter Exception')
                    if 'value' in first_error:
                        error_detail = 'Error found in value=\'{}\'.'.format(first_error['value'])
                    else:
                        error_detail = first_error.get('detail', 'Details not provided.')
                    message = '{}: {}'.format(error_title, error_detail)
                    raise TwitterException(message, errors)
                else:
                    message = 'Invalid Payload: {payload}'.format(payload=response.text)
                    raise TwitterException(message, errors=[])
            except JSONDecodeError as _:
                raise TwitterException('Server responded with status code {}'.format(response.status_code),
                                       [{'code': response.status_code}])
        if stream:
            return self.stream_response(response)
        else:
            try:
                payload = response.json()
            except JSONDecodeError as _:
                message = 'Invalid Payload: {payload}'.format(payload=response.text)
                raise TwitterException(message, errors=[])
            if ('data' not in payload) and ('errors' in payload):
                errors = list(payload['errors'])
                first_error = errors[0] if len(errors) > 0 else {}
                error_title = first_error.get('title', 'Twitter Exception')
                error_detail = first_error.get('detail', first_error.get('details', 'no details provided.'))
                if isinstance(error_detail, list) and len(error_detail) > 0:
                    error_detail = error_detail[0]
                message = '{}: {}'.format(error_title, error_detail)
                raise TwitterException(message, errors)
            self.response = payload
            return payload
