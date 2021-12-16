import collections
import time
import weakref

from six import string_types
from tweetkit.twitter.errors import TwitterException

__all__ = [
    'UserRequest',
    'TweetRequest',
    'TweetStreamRequest',
]

MEDIA_FIELDS = {
    'media.fields': 'duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics',
}

POOL_FIELDS = {
    'poll.fields': 'duration_minutes,end_datetime,id,options,voting_status',
}

PLACE_FIELDS = {
    'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
}

USER_FIELDS = {
    'user.fields': 'created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,'
                   'protected,public_metrics,url,username,verified,withheld',
}

EXPANSIONS = {
    'expansions': 'attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,'
                  'geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id',
}

TWEET_FIELDS = {
    'tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,'
                    'geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,'
                    'reply_settings,source,text,withheld',
}

DEFAULT_TWEET_FIELDS = {
    **EXPANSIONS,
    **TWEET_FIELDS,
    **USER_FIELDS,
    **PLACE_FIELDS,
}


def denormalize(payload):
    included_users = {}
    included_users_by_username = {}
    included_tweets = {}
    included_places = {}
    included_media = {}
    included_polls = {}
    if 'includes' in payload:
        if 'users' in payload['includes']:
            for user in payload['includes']['users']:
                included_users[user['id']] = user
                if 'username' in user:
                    included_users_by_username[user['username']] = included_users_by_username
        if 'tweets' in payload['includes']:
            for tweet in payload['includes']['tweets']:
                included_tweets[tweet['id']] = tweet
        if 'places' in payload['includes']:
            for place in payload['includes']['places']:
                included_places[place['id']] = place
        if 'media' in payload['includes']:
            for media in payload['includes']['media']:
                included_media[media['media_key']] = media
        if 'polls' in payload['includes']:
            for poll in payload['includes']['polls']:
                included_polls[poll['id']] = poll
    many = True
    payload_data = payload.get('data', [])
    if not isinstance(payload_data, collections.Sequence):
        many = False
        payload_data = [payload_data]
    for item in payload_data:
        if 'author_id' in item and item['author_id'] in included_users:
            item['author'] = included_users[item['author_id']]
        if 'referenced_tweets' in item:
            for referenced_tweet in item['referenced_tweets']:
                referenced_tweet_id = referenced_tweet['id']
                if referenced_tweet_id in included_tweets:
                    referenced_tweet_obj = included_tweets[referenced_tweet_id]
                    if 'author_id' in referenced_tweet_obj and referenced_tweet_obj['author_id'] in included_users:
                        referenced_tweet_obj['author'] = included_users[referenced_tweet_obj['author_id']]
                    referenced_tweet['tweet'] = referenced_tweet_obj
        if 'in_reply_to_user_id' in item and item['in_reply_to_user_id'] in included_users:
            in_reply_to_user_id = item['in_reply_to_user_id']
            item['in_reply_to_user'] = included_users[in_reply_to_user_id]
        # attachments.media_keys
        if 'attachments' in item and 'media_keys' in item['attachments']:
            media_attachments = []
            for media_key in item['attachments']['media_keys']:
                if media_key in included_media:
                    media_obj = included_media[media_key]
                    media_attachments.append(media_obj)
            item['attachments']['media'] = media_attachments
        # attachments.poll_ids
        if 'attachments' in item and 'poll_ids' in item['attachments']:
            for poll_id in item['attachments']['poll_ids']:
                poll_attachments = []
                if poll_id in included_polls:
                    poll_obj = included_polls[poll_id]
                    poll_attachments.append(poll_obj)
                item['attachments']['polls'] = poll_attachments
        if 'geo' in item and 'place_id' in item['geo']:
            place_id = item['geo']['place_id']
            if place_id in included_places:
                item['geo']['place'] = included_places[place_id]
        if 'entities' in item and 'mentions' in item['entities']:
            for mention in item['entities']['mentions']:
                if 'username' in mention and mention['username'] in included_users_by_username:
                    mentioned_user = included_users_by_username[mention['username']]
                    mention['user'] = mentioned_user
                elif 'tag' in mention and mention['tag'] in included_users_by_username:
                    mentioned_user = included_users_by_username[mention['tag']]
                    mention['user'] = mentioned_user
        # referenced_tweets.id.author_id (^above)
        if 'pinned_tweet_id' in item:
            pinned_tweet_id = item['pinned_tweet_id']
            if pinned_tweet_id in included_tweets:
                item['pinned_tweet'] = included_tweets[pinned_tweet_id]
    if many:
        return payload_data
    return payload_data[0]


class Request:
    def __init__(self, client):
        self._client = weakref.ref(client)

    @property
    def request(self):
        return self.client.request

    @property
    def client(self) -> 'TwitterClient':
        return self._client()


class UserRequest(Request):
    def __getitem__(self, item):
        return self.get(id=item)

    def get(self, id=None, **kwargs):
        """Returns a variety of information about one or more users specified by the requested IDs.

        :param id: The ID/s of the user/s to lookup.
        :param kwargs: request options as dict
        :return: a user or a list of users
        """
        if (isinstance(id, string_types) and (',' not in id)) or isinstance(id, int):
            id = str(id)
            request_url = 'https://api.twitter.com/2/users/{id}'.format(id=id)
        else:
            if not isinstance(id, string_types):
                id = ','.join([str(x) for x in id])
            request_url = 'https://api.twitter.com/2/users'
            kwargs['ids'] = id
        payload = self.request(request_url, kwargs)
        return denormalize(payload)

    def by(self, username=None, **kwargs):
        """Returns a variety of information about one or more users specified by their usernames.

        :param username: The Twitter username/s (handle/s) of the user.
        :param kwargs: request options as dict
        :return: list of users
        """
        if isinstance(username, string_types) and (',' not in username):
            request_url = 'https://api.twitter.com/2/users/by/username/{username}'.format(username=username)
        else:
            request_url = 'https://api.twitter.com/2/users'
            if not isinstance(username, string_types):
                username = ','.join([str(x) for x in username])
            kwargs['usernames'] = username
        payload = self.request(request_url, kwargs)
        return denormalize(payload)

    def tweets(self, id, **kwargs):
        """Returns Tweets composed by a single user, specified by the requested user ID.

        By default, the most recent ten Tweets are returned per request.
        Using pagination, the most recent 3,200 Tweets can be retrieved.

        :param id: The ID of the user.
        :param kwargs: request options as dict
        :return:
        """
        if (isinstance(id, string_types) and (',' not in id)) or isinstance(id, int):
            id = str(id)
            request_url = 'https://api.twitter.com/2/users/{id}/tweets'.format(id=id)
        else:
            raise TypeError('Invalid type for attribute \'id\'. Expected {}, found {}.'.format(str, type(id)))
        if 'max_results' not in kwargs:
            kwargs['max_results'] = 100
        retry_count = 0
        for k, v in DEFAULT_TWEET_FIELDS.items():
            if k not in kwargs:
                kwargs[k] = v
        while True:
            try:
                payload = self.request(request_url, kwargs)
            except TwitterException as e:
                if retry_count < 3:  # retry three times before raising the error
                    time.sleep(retry_count * 60)
                    retry_count += 1
                else:
                    raise e
            else:
                retry_count = 0
                if ('meta' in payload) and ('result_count' in payload['meta']):
                    if not (payload['meta']['result_count'] > 0):
                        return
                if 'data' in payload:
                    for tweet in denormalize(payload):
                        yield tweet
                if ('meta' in payload) and ('next_token' in payload['meta']):
                    kwargs['pagination_token'] = payload['meta']['next_token']
                else:
                    return


class TweetSearchOptions:
    def __init__(self, func):
        self.func = func
        self.search_mode = 'recent'

    @property
    def all(self):
        options = TweetSearchOptions(self.func)
        options.search_mode = 'all'
        return options

    @property
    def recent(self):
        options = TweetSearchOptions(self.func)
        options.search_mode = 'recent'
        return options

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class TweetRequest(Request):
    @property
    def search(self):
        self.client._request_wait = 3
        return TweetSearchOptions(self._search)

    def get(self, id, **kwargs):
        """Get tweet by it's id

        :param id: id of the tweet
        :param kwargs: other args for request
        :return: tweet object
        """
        if (isinstance(id, string_types) and (',' not in id)) or isinstance(id, int):
            id = str(id)
            request_url = 'https://api.twitter.com/2/tweets/{id}'.format(id=id)
        else:
            raise TypeError('Invalid type for attribute \'id\'. Expected {}, found {}.'.format(str, type(id)))
        for k, v in DEFAULT_TWEET_FIELDS.items():
            if k not in kwargs:
                kwargs[k] = v
        self.client._request_wait = 3
        payload = self.request(request_url, kwargs)
        return denormalize(payload)

    def _search(self, query=None, **kwargs):
        """The recent search endpoint returns Tweets from the last seven days that match a search query.

        :param query: One rule for matching Tweets.
        :param kwargs: request options as dict
        :return:
        """
        search_mode = kwargs.pop('search_mode', 'recent')
        max_retry_count = kwargs.pop('max_retry_count', 3)
        retry_wait_time = kwargs.pop('retry_wait_time', 60)
        if search_mode == 'stream':
            url = 'https://api.twitter.com/2/tweets/search/stream'
        elif search_mode == 'sample':
            url = 'https://api.twitter.com/2/tweets/sample/stream'
        elif search_mode == 'recent':
            url = 'https://api.twitter.com/2/tweets/search/recent'
        else:
            url = 'https://api.twitter.com/2/tweets/search/all'
        if search_mode not in ['stream', 'sample']:
            kwargs['query'] = query
            if ('max_results' not in kwargs) and (search_mode == 'recent'):
                kwargs['max_results'] = 100
            elif 'max_results' not in kwargs:
                kwargs['max_results'] = 500
        retry_count = 0
        for k, v in DEFAULT_TWEET_FIELDS.items():
            if k not in kwargs:
                kwargs[k] = v
        while True:
            try:
                if search_mode in ['stream', 'sample']:
                    responses = self.request(url, kwargs, stream=True)
                    for payload in responses():
                        if payload is None:
                            return
                        yield denormalize(payload)
                else:
                    payload = self.request(url, kwargs)
                    if ('meta' in payload) and ('result_count' in payload['meta']):
                        if not (payload['meta']['result_count'] > 0):
                            return
                    if 'data' in payload:
                        for tweet in denormalize(payload):
                            yield tweet
                    if ('meta' in payload) and ('next_token' in payload['meta']):
                        kwargs['next_token'] = payload['meta']['next_token']
                    else:
                        return
            except TwitterException as e:
                if retry_count < max_retry_count:
                    time.sleep(retry_count * retry_wait_time)
                    retry_count += 1
                else:
                    raise e
            finally:
                pass


class TweetStreamRulesRequest(Request):
    def get(self, id=None, **kwargs):
        request_url = 'https://api.twitter.com/2/tweets/search/stream/rules'
        if id is not None:
            if isinstance(id, (string_types, int)):
                kwargs['ids'] = str(id)
            elif isinstance(id, list):
                kwargs['ids'] = ','.join([str(x) for x in id])
            else:
                error_message = 'Invalid type for attribute id. Expected one of {}, found {}.'
                raise TypeError(error_message.format((int, str, list), type(id)))
        payload = self.request(request_url, kwargs)
        return denormalize(payload)

    def _post(self, data, dry_run=False, **kwargs):
        request_url = 'https://api.twitter.com/2/tweets/search/stream/rules'
        if dry_run:
            kwargs['dry_run'] = True
        payload = self.request(request_url, kwargs, method='POST', data=data)
        return payload

    def add(self, data, dry_run=False, **kwargs):
        if data is None:
            raise ValueError('Data not found.')
        if isinstance(data, list):
            data = list(data)
        payload = self._post({'add': data}, dry_run=dry_run, **kwargs)
        return payload

    def delete(self, data=None, dry_run=False, **kwargs):
        if data is None:
            data = dict(ids=list(map(lambda rule: rule['id'], self.get())))
        payload = self._post({'delete': data}, dry_run=dry_run, **kwargs)
        return payload


class TweetStreamRequest(TweetRequest):
    def __init__(self, client):
        super().__init__(client)
        self.rules = TweetStreamRulesRequest(self)

    def __call__(self, mode='sample', max_retry_count=1, retry_wait_time=1):
        self.client._request_wait = 18
        if mode not in ['stream', 'sample']:
            raise ValueError('Invalid search mode, expected {} found (stream, sample)'.format(mode))
        kwargs = dict(
            search_mode=mode,
            max_retry_count=max_retry_count,
            retry_wait_time=retry_wait_time
        )
        return self._search(**kwargs)
