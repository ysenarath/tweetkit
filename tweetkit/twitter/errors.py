__all__ = [
    'TwitterException',
]


class TwitterException(Exception):
    def __init__(self, message, errors=None):
        super(TwitterException, self).__init__(message)
        if errors is None:
            errors = []
        self.message = message
        self.errors = errors

    def __repr__(self):
        return self.message
