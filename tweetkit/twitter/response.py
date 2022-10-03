"""Generic response object."""

__all__ = [
    'Response'
]


class Response(object):
    """Response"""

    def __init__(self, data, message=None):
        self._data = data
        self._message = message

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
