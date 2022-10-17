"""Response"""
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

    def __init__(self, content, dtype=None, **kwargs):
        self._response = kwargs.get('response', None)
        if isinstance(content, requests.Response):
            self._response = content
        self._content = json.loads(content)
        try:
            data = self._content['data']
        except KeyError as ex:
            # for loading result of endpoint '/2/openapi.json'
            data = self._content
        self._data = data
        errors = self._content.get('errors', None)
        if isinstance(errors, collections.Mapping):
            errors = [errors]
        if errors is not None:
            errors = list(map(TwitterProblem, errors))
        self._errors = errors
        self._meta = self._content.get('meta', dict())
        self._includes = self._content.get('includes', None)
        self._dtype = dtype

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
    def data(self):
        """Gets data."""
        return self._data

    @property
    def includes(self):
        """Gets includes."""
        return self._includes

    @property
    def errors(self):
        """Gets errors of the response data object.

        Returns
        -------
        errors: list of Problem
            A list of problem (Exception) objects.
        """
        return self._errors

    @property
    def meta(self):
        """meta"""
        return self._meta

    @property
    def dtype(self):
        """Gets includes."""
        return self._dtype

    def __getitem__(self, item):
        """Gets value from 'data' with provided item as key."""
        if isinstance(self._data, list):
            return [data[item] for data in self._data]
        return self._data[item]

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


class TwitterStreamResponse(object):
    """TwitterStreamResponse"""

    def __init__(self, iter, **kwargs):
        self._response = None
        if isinstance(iter, requests.Response):
            if iter.encoding is None:
                iter.encoding = 'utf-8'
            self._response = iter
            iter = iter.iter_lines(decode_unicode=True)
        self._iter = iter
        self._kwargs = kwargs

    def __next__(self):
        line = None
        while line is not None and len(line.strip()) > 0:
            line = next(self._iter)
        return TwitterResponse(line, response=self._response, **self._kwargs)

    def __iter__(self):
        return self

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
