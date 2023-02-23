"""TwitterException"""
import collections
import json as simplejson

import requests

__all__ = {
    'TwitterException',
    'TwitterRequestException',
    'TwitterTimeoutException',
    'JSONDecodeError',
    'TwitterError',
    'TwitterProblem',
    'ProblemOrError',
}


class TwitterException(collections.UserDict, Exception):
    """TwitterException"""

    __default_message__ = 'a problem occurred, unknown reason'

    def __init__(self, *args, **kwargs):
        collections.UserDict.__init__(self, kwargs)
        if len(args) == 0:
            args = (self.message,)
        Exception.__init__(self, *args)

    def __getattr__(self, item):
        if item in self:
            return self.get(item)
        raise AttributeError('\'{}\' object has no attribute \'{}\''.format(type(self).__name__, item))

    @property
    def message(self):
        """Gets the message provided in message field.

        This value will be overridden by kwargs provided.

        Returns
        -------
        message: str
            The message.
        """
        if 'message' in self:
            return self.get('message')
        if hasattr(self, 'args') and len(self.args) > 0:
            return self.args[0]
        return self.__default_message__


class TwitterRequestException(TwitterException, requests.exceptions.RequestException):
    """There was an ambiguous exception that occurred while handling your request."""

    def __init__(self, *args, **kwargs):
        """Initialize RequestException with `request` and `response` objects."""
        response = None
        if len(args) > 0 and isinstance(args[0], requests.Response):
            response, args = args[0], args[1:]
            # remove response from kwargs if still exists
            kwargs_response = None
            if 'response' in kwargs:
                kwargs_response = kwargs.pop('response')
            if response is None:  # and kwargs_response is not None
                response = kwargs_response
        elif 'response' in kwargs and isinstance(kwargs['response'], requests.Response):
            response = kwargs.pop('response')
        # extract request if available as kwargs or through response
        request = kwargs.pop('request', None)
        if response is not None and not request and hasattr(response, 'request'):
            request = response.request
        # update kwargs data by parsing response data
        if response is not None and isinstance(response, requests.Response):
            for key, value in json.loads(response).items():
                if key is not None:
                    kwargs[key] = value
        # extract dict data from arg if provided (if response is provided as arg it should be first)
        if len(args) > 0 and isinstance(args[0], collections.Mapping):
            data, args = args[0], args[1:]
            kwargs.update(data)
        super(TwitterRequestException, self).__init__(*args, **kwargs, request=request, response=response)

    @property
    def code(self):
        """Gets code.

        Returns
        -------
        code: int
            The status code.
        """
        if 'code' in self:
            return self.get('code')
        if self.response is not None and isinstance(self.response, requests.Response):
            return self.response.status_code
        return None


class TwitterTimeoutException(TwitterRequestException, requests.exceptions.Timeout):
    pass


class JSONDecodeError(TwitterException, simplejson.JSONDecodeError):
    """JSONDecodeError"""
    pass


from tweetkit.utils import json


class TwitterError(TwitterRequestException):
    """TwitterError"""
    __default_message__ = 'an error occurred, unknown reason',

    def __init__(self, *args, **kwargs):
        super(TwitterError, self).__init__(*args, **kwargs)


class TwitterProblem(TwitterRequestException):
    """TwitterProblem"""

    __default_message__ = 'a problem occurred, unknown reason'

    def __init__(self, *args, **kwargs):
        super(TwitterProblem, self).__init__(*args, **kwargs)

    @property
    def message(self):
        """Gets the message from detail field of twitter problem response.

        Returns
        -------
        message: str
            The message.
        """
        if 'detail' in self:
            return self.get('detail')
        if 'title' in self:
            return self.get('title')
        return super(TwitterProblem, self).message

    @property
    def code(self):
        """Gets code from status field of twitter problem response.

        Returns
        -------
        code: int
            The status code.
        """
        if 'status' in self:
            return self.get('status')
        return super(TwitterProblem, self).code


def ProblemOrError(*args, **kwargs):  # noqa
    """Create Problem or Error.

    Returns
    -------
    error: TwitterError or TwitterProblem
        Returns error or problem.
    """
    response = kwargs.get('response', args[0])
    content_type = response.headers.get('content-type')
    if content_type.startswith(('application/json', 'application/problem+json')):
        data = json.loads(response)
        if 'code' in data and 'message' in data:
            return TwitterError(response)
        if 'type' in data and 'title' in data:
            return TwitterProblem(response)
    return None
