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
        self._response = None
        if isinstance(content, requests.Response):
            self._response = content
        elif 'response' in kwargs:
            self._response = kwargs['response']
        content = json.loads(content)
        errors = content.get('errors', None)
        if isinstance(errors, collections.Mapping):
            errors = [errors]
        self._errors = errors
        self._meta = content.get('meta', None)
        self._includes = content.get('includes', None)
        try:
            data = content['data']
        except KeyError as ex:
            # for loading result of endpoint '/2/openapi.json'
            data = content
        self._data = data
        self._dtype = dtype

    @property
    def data(self):
        """Gets data from the response.

        Returns
        -------
        dict
            The data of response.
        """
        return self._data

    @property
    def includes(self):
        """Gets includes from the response.

        Returns
        -------
        dict
            The includes of response.
        """
        return self._includes

    @property
    def dtype(self):
        """Gets data-type of the response.

        Returns
        -------
        str
            The data-type of response.
        """
        return self._dtype

    @property
    def errors(self):
        """Gets errors from the response.

        Returns
        -------
        list of TwitterProblem
            The errors of response.
        """
        if self._errors is not None:
            return list(map(TwitterProblem, self._errors))
        else:
            return None

    @property
    def meta(self):
        """Gets errors from the response.

        Returns
        -------
        dict
            The errors component of response.
        """
        return self._meta

    def get(self, item, default=None):
        """Gets item from data. Returns list if there are multiple objects in data.

        Parameters
        ----------
        item: str
            The key to extract the data.
        default: typing.Any
            The default return value.
        Returns
        -------
        The data item referred by the provided key.
        """
        if isinstance(self.data, collections.Sequence) and not isinstance(self.data, str):
            return list(map(lambda d: d.get(item, default), self.data))
        return self.data.get(item, default)

    def __repr__(self):
        return self.to_json(indent=2)

    def to_json(self, path_or_buf=None, *args, **kwarg):
        """Convert the object to a JSON string.

        Parameters
        ----------
        path_or_buf: str, path object, file-like object, or None, default None
            String, path object (implementing os.PathLike[str]), or file-like
            object implementing a write() function. If None, the result is
            returned as a string.

        Returns
        -------
        None or str
            If path_or_buf is None, returns the resulting json format as a
            string. Otherwise returns None.
        """
        if path_or_buf is not None:
            return json.dump(self.content, path_or_buf, *args, **kwarg)
        return json.dumps(self.content, *args, **kwarg)

    @property
    def content(self):
        """Gets list of objects or object dict."""
        content = {
            'data': self._data,
            'includes': self._includes,
            'errors': self._errors,
            'meta': self._meta,
            'dtype': self._dtype,
        }
        if isinstance(content['data'], collections.Mapping):
            return content
        else:
            results = []
            for data in content['data']:
                result = content.copy()
                result['data'] = data
                results.append(result)
            return results


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
        while line is None or len(line.strip()) < 1:
            line = next(self._iter)
        return TwitterResponse(line, response=self._response, **self._kwargs)

    def __iter__(self):
        return self

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

    @property
    def content(self):
        """Iterator of objects."""
        for response in self:
            content = response.content
            if isinstance(content, collections.Mapping):
                yield content
            else:
                for item in content:
                    yield item
