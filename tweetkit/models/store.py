"""ObjectStore"""
import collections

from tweetkit.utils import copy

__all__ = [
    'ObjectStore'
]


class ObjectStore(object):
    """ObjectStore"""

    index_by = {
        'media': 'media_key',
        'places': 'id',
        'polls': 'id',
        'topics': 'id',
        'tweets': 'id',
        'users': 'id',
        'lists': 'id',
        'Space': 'id',
    }

    mappings = {
        'Media': 'media',
        'Place': 'places',
        'Poll': 'polls',
        'Topic': 'topics',
        'Tweet': 'tweets',
        'User': 'users',
        'List': 'lists',
        'Space': 'spaces',
    }

    def __init__(self, resp):
        self.store = {}
        self._next_id = 0
        if resp.includes is not None:
            self.update(resp.includes)
        self.add(resp.data, dtype=resp.dtype)

    @property
    def next_id(self):
        """next_id"""
        next_id = self._next_id
        self._next_id += 1
        return next_id

    def add(self, data, dtype=None):
        """Add to index."""
        if isinstance(data, collections.Sequence):
            for item in data:
                self.add(item, dtype=dtype)
        elif isinstance(data, collections.Mapping):
            if dtype in self.mappings:
                store_key = self.mappings[dtype]
            else:
                store_key = dtype
            if store_key not in self.store:
                self.store[store_key] = {}
            if store_key in self.index_by:
                id_ = data[self.index_by[store_key]]
            else:
                id_ = self.next_id
            self.store[store_key][id_] = data
        else:
            raise TypeError('expected dict or list, found {}'.format(type(self.store).__name__))

    def update(self, other):
        """Updates from other."""
        if isinstance(other, ObjectStore):
            other = other.store
        for key in other.keys():
            self.add(other[key], dtype=key)
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
