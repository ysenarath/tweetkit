"""TwitterException"""
import json as simplejson

import requests

__all__ = {
    'TwitterException',
    'TwitterError',
    'TwitterProblem',
    'RequestException',
    'JSONDecodeError',
}


def process_args(*args, **kwargs):
    """Extract response from arguments and try to decode it and add as args.

    Parameters
    ----------
    args
        Args.
    kwargs
        Kwargs.

    Returns
    -------
    args:
        Args.
    kwargs:
        Kwargs.
    """
    response = None
    if 'response' in kwargs and isinstance(kwargs['response'], requests.Response):
        response = kwargs.pop('response')
    elif len(args) > 0 and isinstance(args[0], requests.Response):
        response, args = args[0], args[1:]
    kwargs['response'] = response
    # process request
    request = kwargs.pop('request', None)
    if response is not None and not request and hasattr(response, 'request'):
        request = response.request
    kwargs['request'] = request
    return args, kwargs


class TwitterException(Exception):
    """TwitterException"""

    def __init__(self, *args, **kwargs):
        super(TwitterException, self).__init__(*args)
        self._attrs = kwargs

    def __getitem__(self, item):
        return self._attrs[item]

    def __getattr__(self, item):
        if item not in self._attrs:
            raise AttributeError('\'{}\' object has no attribute \'{}\''.format(type(self).__name__, item))
        return self._attrs[item]

    @property
    def message(self):
        """Gets message.

        Returns
        -------
        message: str
            The message.
        """
        return self.args[0]

    @property
    def code(self):
        """Gets code.

        Returns
        -------
        code: int
            The code.
        """
        return self.args[1]


class JSONDecodeError(TwitterException, simplejson.JSONDecodeError):
    """JSONDecodeError"""
    pass


from tweetkit.utils import json


class TwitterError(TwitterException):
    """TwitterError"""

    default_message = 'an error occurred, unknown reason'

    def __init__(self, *args, **kwargs):
        # process args
        args, kwargs = process_args(*args, **kwargs)
        response = kwargs.get('response')
        if response is not None:
            for key, value in json.loads(response).items():
                if key not in kwargs:
                    kwargs[key] = value
        # process args
        args, kwargs = process_args(*args, **kwargs)
        default_message = args[0] if len(args) > 0 else self.default_message
        message = kwargs.get('message', default_message)
        default_code = args[1] if len(args) > 1 else None
        code = kwargs.get('code', default_code)
        kwargs = {key: value for key, value in kwargs.items() if key not in ['code', 'message']}
        super(TwitterError, self).__init__(message, code, **kwargs)


class TwitterProblem(TwitterException):
    """TwitterProblem"""

    default_message = 'a problem occurred, unknown reason'

    def __init__(self, *args, **kwargs):
        # process args
        args, kwargs = process_args(*args, **kwargs)
        response = kwargs.get('response')
        if response is not None:
            for key, value in json.loads(response).items():
                if key not in kwargs:
                    kwargs[key] = value
        # extract message from detail
        message = kwargs.get('detail', args[0] if len(args) > 0 else self.default_message)
        # extract status
        code = kwargs.get('status', args[1] if len(args) > 1 else None)
        # twitter problem
        super(TwitterProblem, self).__init__(message, code, **kwargs)


class RequestException(TwitterException, requests.exceptions.RequestException):
    """There was an ambiguous exception that occurred while handling your request."""

    def __init__(self, *args, **kwargs):
        """ Initialize RequestException with `request` and `response` objects."""
        # process args
        args, kwargs = process_args(*args, **kwargs)
        super(RequestException, self).__init__(*args, **kwargs)
