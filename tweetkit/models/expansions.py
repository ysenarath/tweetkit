"""ObjectStore"""
import collections

from tweetkit.utils import copy

__all__ = [
    'TwitterExpansions',
]

index_by = {
    'media': 'media_key',
    'places': 'id',
    'polls': 'id',
    'topics': 'id',
    'tweets': 'id',
    'users': 'id',
    'lists': 'id',
    'spaces': 'id',
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


class TwitterExpansions(object):
    """TwitterExpansions"""

    def __init__(self, includes=None, **kwargs):
        self._includes = {store_key: {} for store_key in index_by.keys()}
        if includes is None:
            includes = {}
        if 'includes' in includes:
            includes = includes['includes']
        for key, value in includes.items():
            self.add(value, dtype=key)
        self._next_id = 0

    @property
    def next_id(self):
        """next_id"""
        self._next_id += 1
        return self._next_id

    def add(self, data, dtype=None):
        """Add to index."""
        if data is None:
            return
        if isinstance(data, collections.Sequence):
            for item in data:
                self.add(item, dtype=dtype)
        elif isinstance(data, collections.Mapping):
            if dtype in mappings:
                store_key = mappings[dtype]
            else:
                store_key = dtype
            if store_key not in self._includes:
                self._includes[store_key] = {}
            if store_key in index_by:
                id_ = data[index_by[store_key]]
            else:
                id_ = self.next_id
            self._includes[store_key][id_] = data
        else:
            raise TypeError('expected dict or list, found {}'.format(type(data).__name__))

    def get_includes(self, data):
        """Gets mapping of includes used in the provided data."""
        if not isinstance(data, collections.Mapping):
            raise TypeError('expected dict, found {}'.format(type(data).__name__))
        expansions = TwitterExpansions()
        if 'attachments' in data:
            attachments = data['attachments']
            if 'poll_ids' in attachments:
                poll_ids = attachments['poll_ids']
                for poll_id in poll_ids:
                    poll = self._includes['polls'].get(poll_id)
                    expansions.add(poll, dtype='Poll')
            if 'media_keys' in attachments:
                media_keys = attachments['media_keys']
                for media_key in media_keys:
                    media_ = self._includes['media'].get(media_key)
                    expansions.add(media_, dtype='Media')
        if 'referenced_tweets' in data:
            referenced_tweets = data['referenced_tweets']
            for referenced_tweet in referenced_tweets:
                referenced_tweet_id = referenced_tweet['id']
                tweet_ = self._includes['tweets'].get(referenced_tweet_id)
                expansions.add(tweet_, dtype='Tweet')
        if 'author_id' in data:
            author_id = data['author_id']
            user = self._includes['users'].get(author_id)
            expansions.add(user, dtype='User')
        if 'in_reply_to_user_id' in data:
            in_reply_to_user_id = data['in_reply_to_user_id']
            user = self._includes['users'].get(in_reply_to_user_id)
            expansions.add(user, dtype='User')
        if 'geo' in data and 'place_id' in data['geo']:
            place_id = data['geo']['place_id']
            place = self._includes['places'].get(place_id)
            expansions.add(place, dtype='Place')
        if 'pinned_tweet_id' in data:
            pinned_tweet_id = data['pinned_tweet_id']
            tweet_ = self._includes['tweets'].get(pinned_tweet_id)
            expansions.add(tweet_, dtype='Tweet')
        if 'host_ids' in data:
            host_ids = data['host_ids']
            for host_id in host_ids:
                host = self._includes['users'].get(host_id)
                expansions.add(host, dtype='User')
        if 'invited_user_ids' in data:
            invited_user_ids = data['invited_user_ids']
            for invited_user_id in invited_user_ids:
                invited_user = self._includes['users'].get(invited_user_id)
                expansions.add(invited_user, dtype='User')
        if 'speaker_ids' in data:
            speaker_ids = data['speaker_ids']
            for speaker_id in speaker_ids:
                speaker = self._includes['users'].get(speaker_id)
                expansions.add(speaker, dtype='User')
        if 'owner_id' in data:
            owner_id = data['owner_id']
            owner = self._includes['users'].get(owner_id)
            expansions.add(owner, dtype='User')
        includes = {}
        for key, val in expansions._includes.items():
            if len(val) > 0:
                includes[key] = list(val.values())
        return includes

    def expand(self, data, dtype=None):
        """Creates a copy with expanded outputs."""
        if isinstance(data, collections.Sequence) and not isinstance(data, str):
            return [self.expand(item, dtype=dtype) for item in data]
        if not isinstance(data, collections.MutableMapping):
            raise TypeError('expected list or dict, found {}'.format(type(data).__name__))
        data = copy.deepcopy(data)
        if dtype is None or dtype == 'Tweet':
            if 'attachments' in data:
                attachments = data['attachments']
                polls = []
                if 'poll_ids' in attachments:
                    poll_ids = attachments['poll_ids']
                    for poll_id in poll_ids:
                        poll = self._includes['polls'].get(poll_id)
                        polls.append(poll)
                data['attachments']['polls'] = polls
                media = []
                if 'media_keys' in attachments:
                    media_keys = attachments['media_keys']
                    for media_key in media_keys:
                        media_ = self._includes['media'].get(media_key)
                        media.append(media_)
                data['attachments']['media'] = media
            if 'referenced_tweets' in data:
                referenced_tweets = data['referenced_tweets']
                referenced_tweets_ = []
                for referenced_tweet in referenced_tweets:
                    referenced_tweet_id = referenced_tweet['id']
                    if data['id'] == referenced_tweet_id:
                        tweet_ = data
                    else:
                        tweet_ = self._includes['tweets'].get(referenced_tweet_id)
                    referenced_tweet['tweet'] = tweet_
                    referenced_tweets_.append(tweet_)
                data['referenced_tweets'] = referenced_tweets_
            if 'author_id' in data:
                author_id = data['author_id']
                data['author'] = self._includes['users'].get(author_id)
            if 'in_reply_to_user_id' in data:
                in_reply_to_user_id = data['in_reply_to_user_id']
                data['in_reply_to_user'] = self._includes['users'].get(in_reply_to_user_id)
            if 'geo' in data and 'place_id' in data['geo']:
                place_id = data['geo']['place_id']
                data['geo']['place'] = self._includes['places'].get(place_id)
        elif dtype is None or dtype == 'User':
            if 'pinned_tweet_id' in data:
                pinned_tweet_id = data['pinned_tweet_id']
                data['pinned_tweet'] = self._includes['tweets'].get(pinned_tweet_id)
        elif dtype is None or dtype == 'Space':
            if 'host_ids' in data:
                host_ids = data['host_ids']
                hosts = []
                for host_id in host_ids:
                    host = self._includes['users'].get(host_id)
                    hosts.append(host)
                data['hosts'] = hosts
            if 'invited_user_ids' in data:
                invited_user_ids = data['invited_user_ids']
                invited_users = []
                for invited_user_id in invited_user_ids:
                    invited_user = self._includes['users'].get(invited_user_id)
                    invited_users.append(invited_user)
                data['invited_users'] = invited_users
            if 'speaker_ids' in data:
                speaker_ids = data['speaker_ids']
                speakers = []
                for speaker_id in speaker_ids:
                    speaker = self._includes['users'].get(speaker_id)
                    speakers.append(speaker)
                data['speakers'] = speakers
        elif dtype is None or dtype == 'List':
            if 'owner_id' in data:
                owner_id = data['owner_id']
                owner = self._includes['users'].get(owner_id)
                data['owner'] = owner
        elif dtype is None or dtype == 'Media':
            if 'owner_id' in data:
                owner_id = data['owner_id']
                owner = self._includes['users'].get(owner_id)
                data['owner'] = owner
        elif dtype is None or dtype == 'Place':
            if 'owner_id' in data:
                owner_id = data['owner_id']
                owner = self._includes['users'].get(owner_id)
                data['owner'] = owner
        elif dtype is None or dtype == 'Poll':
            pass
        return data
