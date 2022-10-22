"""Paginator"""
import collections

__all__ = [
    'Paginator',
]


class Paginator(object):
    """Paginator."""

    def __init__(self, request):
        self.request = request
        self.next_token = None
        self.has_next = True
        self.errors = []

    def __next__(self):
        if not self.has_next:
            raise StopIteration()
        try:
            self.request.query['next_token'] = self.next_token
            resp = self.request.send()
        except Exception as ex:
            raise ex
        else:
            self.next_token = resp.meta.get('next_token')
            self.has_next = self.next_token is not None
            return resp

    def __iter__(self):
        self.next_token = None
        self.has_next = True
        return self

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
