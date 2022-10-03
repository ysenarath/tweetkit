"""TwitterException"""

__all__ = {
    'TwitterException',
    'TwitterError',
    'TwitterProblem',
}


class TwitterException(Exception):
    """TwitterException"""
    pass


class TwitterError(TwitterException):
    """TwitterError"""

    def __init__(self, *args, **kwargs):
        message = kwargs.get('message', args[0] if len(args) > 0 else None)
        super(TwitterError, self).__init__(message)


class TwitterProblem(TwitterException):
    """TwitterProblem"""

    def __init__(self, *args, **kwargs):
        message = kwargs.get('message', args[0] if len(args) > 0 else None)
        super(TwitterProblem, self).__init__(message)
