"""Generic response object."""
import collections

import requests

from tweetkit.exceptions import TwitterProblem
from tweetkit.utils import json

__all__ = [
    'TwitterObject',
    'TwitterObjectStream',
]


class TwitterObject(object):
    """TwitterObject"""

    def __init__(self, data):
        data = json.loads(data)
        try:
            self._data = data['data']
        except KeyError as ex:
            # for loading result of endpoint '/2/openapi.json'
            self._data = data
        else:
            errors = data.get('errors', [])
            if isinstance(errors, collections.Mapping):
                errors = [errors]
            self._errors = list(map(TwitterProblem, errors))

    @property
    def errors(self):
        """Gets errors of the response data object.

        Returns
        -------
        errors: list of Problem
            A list of problem (Exception) objects.
        """
        return self._errors

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getattr__(self, item):
        if item not in self._data:
            raise AttributeError
        return self[item]

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
        return self._data.get(item, default)


class TwitterObjectStream(object):
    """TwitterObjectStream"""

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
                yield TwitterObject(line)

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
