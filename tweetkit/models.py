"""Generic response object."""
import collections

import requests

from tweetkit.exceptions import TwitterProblem
from tweetkit.utils import json

__all__ = [
    'TwitterResponse',
    'TwitterStreamResponse',
]


class TwitterResponse(object):
    """TwitterResponse"""

    def __init__(self, content, **kwargs):
        self._response = kwargs.get('response', None)
        if isinstance(content, requests.Response):
            self._response = content
        self._content = json.loads(content)
        errors = self._content.pop('errors', None)
        if isinstance(errors, collections.Mapping):
            errors = [errors]
        if errors is not None:
            errors = list(map(TwitterProblem, errors))
        self._errors = errors
        self._meta = self._content.pop('meta', None)
        self._includes = self._content.pop('includes', None)
        try:
            data = self._content['data']
        except KeyError as ex:
            # for loading result of endpoint '/2/openapi.json'
            data = self._content
        self._data = data

    @property
    def response(self):
        """Gets base response of data object.

        Returns
        -------
        response: requests.Response
            The requests.Response object associated with this twitter response.
        """
        return self._response

    @property
    def errors(self):
        """Gets errors of the response data object.

        Returns
        -------
        errors: list of Problem
            A list of problem (Exception) objects.
        """
        return self._errors

    def get(self, item, default=None):
        """Gets item from the request content.

        Parameters
        ----------
        item: str
            The key of item to get.
        default: object
            The default value if item is not present.
        Returns
        -------
        result: object
            The resulting item.
        """
        if isinstance(self._data, list):
            return [data.get(item, default) for data in self._data]
        return self._data.get(item, default)

    def __getitem__(self, item):
        """Gets value from 'data' with provided item as key."""
        return self._data[item]

    def __getattr__(self, item):
        """Gets value from 'data' with provided attr as key."""
        try:
            return self[item]
        except KeyError as ex:
            raise AttributeError('\'{}\' object has no attribute \'{}\''.format(type(self).__name__, item))


class TwitterStreamResponse(object):
    """TwitterStreamResponse"""

    def __init__(self, iter):
        self._response = None
        if isinstance(iter, requests.Response):
            self._response = iter
            if iter.encoding is None:
                iter.encoding = 'utf-8'
            iter = iter.iter_lines(decode_unicode=True)
        self._iter = iter

    def __iter__(self):
        for line in self._iter:
            if line is not None and len(line.strip()) > 0:
                yield TwitterResponse(line, response=self._response)

    def tolist(self):
        """Converts stream to list of response objects.

        Returns
        -------
        responses: list of Response
            The stream as list.
        """
        return list(self)

    def close(self):
        """Close the object.

        Returns
        -------
        None
        """
        if self._response is not None:
            self._response.close()
            return True
        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
