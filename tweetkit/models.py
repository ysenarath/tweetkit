"""Generic response object."""
import collections

import requests

from tweetkit.exceptions import TwitterProblem
from tweetkit.utils import json, copy

__all__ = [
    'TwitterResponse',
    'TwitterStreamResponse',
    'ObjectStore',
]


class Index(object):
    """Index"""

    def __init__(self, key):
        self.key = key
        self.index = {}

    def get(self, key, default=None):
        """Index.get(self, item)"""
        return self.index.get(key, default)

    def add(self, doc):
        """Index.put(self, item)"""
        self.index[doc[self.key]] = copy.deepcopy(doc)

    def __iter__(self):
        for _, value in self.index.items():
            yield value


class ObjectStore(object):
    """ObjectStore"""

    store_key = {
        'Media': 'media',
        'Place': 'places',
        'Poll': 'polls',
        'Topic': 'topics',
        'Tweet': 'tweets',
        'User': 'users',
        'List': 'lists',
        'Space': 'spaces',
    }

    def __init__(self):
        self.store = dict(
            media=Index('media_key'),
            places=Index('id'),
            polls=Index('id'),
            topics=Index('id'),
            tweets=Index('id'),
            users=Index('id'),
            lists=Index('id'),
            spaces=Index('id'),
        )

    def __getattr__(self, item):
        try:
            return self.store[item]
        except KeyError as ex:
            raise AttributeError('\'{}\' object has no attribute \'{}\''.format(type(self).__name__, item))

    def add(self, data, dtype=None):
        """Add to index."""
        key = self.store_key[dtype]
        idx = self.store.get(key)
        if idx is not None:
            if isinstance(data, collections.Sequence) and not isinstance(data, str):
                for item in data:
                    idx.add(item)
            else:
                idx.add(data)

    def update(self, other):
        """Update."""
        if isinstance(other, collections.Mapping):
            for key in other.keys():
                if key not in self.store.keys():
                    raise KeyError('unable to index objects of type \'{}\''.format(key))
        for key in self.store.keys():
            objs = None
            if isinstance(other, ObjectStore):
                objs = other.store[key]
            elif isinstance(other, collections.Mapping) and key in other:
                objs = other[key]
            if objs is not None:
                if isinstance(objs, collections.Mapping):
                    objs = objs,
                for obj in objs:
                    self.store[key].add(obj)
        return self

    def resolve(self, data, dtype=None):
        """Resolve."""
        if isinstance(data, collections.Sequence) and not isinstance(data, str):
            return [self.resolve(item, dtype=dtype) for item in data]
        if not isinstance(data, collections.MutableMapping):
            raise TypeError('expected list or dict, found {}'.format(type(data).__name__))
        data = copy.deepcopy(data)
        if dtype == 'Tweet':
            if 'attachments' in data:
                attachments = data['attachments']
                polls = []
                if 'poll_ids' in attachments:
                    poll_ids = attachments['poll_ids']
                    for poll_id in poll_ids:
                        poll = self.store['polls'].get(poll_id)
                        polls.append(poll)
                data['attachments']['polls'] = polls
                media = []
                if 'media_keys' in attachments:
                    media_keys = attachments['media_keys']
                    for media_key in media_keys:
                        media_ = self.store['media'].get(media_key)
                        media.append(media_)
                data['attachments']['media'] = media
            if 'referenced_tweets' in data:
                referenced_tweets = data['referenced_tweets']
                referenced_tweets_ = []
                for referenced_tweet in referenced_tweets:
                    referenced_tweet_id = referenced_tweet['id']
                    tweet_ = self.store['tweets'].get(referenced_tweet_id)
                    referenced_tweet['tweet'] = tweet_
                    referenced_tweets_.append(tweet_)
                data['referenced_tweets'] = referenced_tweets_
            if 'author_id' in data:
                author_id = data['author_id']
                data['author'] = self.store['users'].get(author_id)
            if 'in_reply_to_user_id' in data:
                in_reply_to_user_id = data['in_reply_to_user_id']
                data['in_reply_to_user'] = self.store['users'].get(in_reply_to_user_id)
            if 'geo' in data and 'place_id' in data['geo']:
                place_id = data['geo']['place_id']
                data['geo']['place'] = self.store['places'].get(place_id)
        elif dtype == 'User':
            if 'pinned_tweet_id' in data:
                pinned_tweet_id = data['pinned_tweet_id']
                data['pinned_tweet'] = self.store['tweets'].get(pinned_tweet_id)
        elif dtype == 'Space':
            if 'host_ids' in data:
                host_ids = data['host_ids']
                hosts = []
                for host_id in host_ids:
                    host = self.store['users'].get(host_id)
                    hosts.append(host)
                data['hosts'] = hosts
            if 'invited_user_ids' in data:
                invited_user_ids = data['invited_user_ids']
                invited_users = []
                for invited_user_id in invited_user_ids:
                    invited_user = self.store['users'].get(invited_user_id)
                    invited_users.append(invited_user)
                data['invited_users'] = invited_users
            if 'speaker_ids' in data:
                speaker_ids = data['speaker_ids']
                speakers = []
                for speaker_id in speaker_ids:
                    speaker = self.store['users'].get(speaker_id)
                    speakers.append(speaker)
                data['speakers'] = speakers
        elif dtype == 'List':
            if 'owner_id' in data:
                owner_id = data['owner_id']
                owner = self.store['users'].get(owner_id)
                data['owner'] = owner
        elif dtype == 'Media':
            if 'owner_id' in data:
                owner_id = data['owner_id']
                owner = self.store['users'].get(owner_id)
                data['owner'] = owner
        elif dtype == 'Place':
            if 'owner_id' in data:
                owner_id = data['owner_id']
                owner = self.store['users'].get(owner_id)
                data['owner'] = owner
        elif dtype == 'Poll':
            pass
        return data


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
        self._meta = self._content.get('meta', None)
        self._includes = self._content.get('includes', None)
        self._dtype = dtype
        store = ObjectStore()
        if self._includes is not None:
            store.update(self._includes)
        store.add(data, dtype=dtype)
        self._store = store

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

    @property
    def data(self):
        """Gets data."""
        return self._store.resolve(self._data, dtype=self._dtype)

    def __getitem__(self, item):
        """Gets value from 'data' with provided item as key."""
        return self._data[item]


class TwitterStreamResponse(object):
    """TwitterStreamResponse"""

    def __init__(self, iter, **kwargs):
        self._response = None
        if isinstance(iter, requests.Response):
            self._response = iter
            if iter.encoding is None:
                iter.encoding = 'utf-8'
            iter = iter.iter_lines(decode_unicode=True)
        self._iter = iter
        self._kwargs = kwargs

    def __iter__(self):
        for line in self._iter:
            if line is not None and len(line.strip()) > 0:
                yield TwitterResponse(line, response=self._response, **self._kwargs)

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
