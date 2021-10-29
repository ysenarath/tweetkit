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
    **TWEET_FIELDS,
    **EXPANSIONS,
    **USER_FIELDS,
    **PLACE_FIELDS,
}


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
        response = self.request(request_url, kwargs)
        return response['data']

    def __getitem__(self, item):
        return self.get(id=item)

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
        response = self.request(request_url, kwargs)
        return response['data']

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
                response = self.request(request_url, kwargs)
            except TwitterException as e:
                if retry_count < 3:  # retry three times before raising the error
                    time.sleep(retry_count * 60)
                    retry_count += 1
                else:
                    raise e
            else:
                retry_count = 0
                if ('meta' in response) and ('result_count' in response['meta']):
                    if not (response['meta']['result_count'] > 0):
                        return
                if 'data' in response:
                    for tweet in response['data']:
                        yield tweet
                if ('meta' in response) and ('next_token' in response['meta']):
                    kwargs['pagination_token'] = response['meta']['next_token']
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
        return payload['data']

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
                    for response in responses():
                        if response is None:
                            return
                        yield response['data']
                else:
                    response = self.request(url, kwargs)
                    if ('meta' in response) and ('result_count' in response['meta']):
                        if not (response['meta']['result_count'] > 0):
                            return
                    if 'data' in response:
                        for tweet in response['data']:
                            yield tweet
                    if ('meta' in response) and ('next_token' in response['meta']):
                        kwargs['next_token'] = response['meta']['next_token']
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
                raise AttributeError(
                    'Invalid type for attribute id. Expected one of {}, found {}.'.format((int, str, list), type(id)))
        payload = self.request(request_url, kwargs)
        if 'data' in payload:
            return payload['data']
        else:
            return []

    def _post(self, data, dry_run=False, **kwargs):
        request_url = 'https://api.twitter.com/2/tweets/search/stream/rules'
        if dry_run:
            kwargs['dry_run'] = True
        payload = self.request(request_url, kwargs, method='POST', data=data)
        return payload

    def add(self, data, dry_run=False, **kwargs):
        payload = self._post({'add': data}, dry_run=dry_run, **kwargs)
        return payload['data']

    def delete(self, data=None, dry_run=False, **kwargs):
        if data is None:
            data = dict(ids=list(map(lambda rule: rule['id'], self.get())))
        payload = self._post({'delete': data}, dry_run=dry_run, **kwargs)
        return payload['meta']


class TweetStreamRequest(TweetRequest):
    def __init__(self, client):
        super().__init__(client)
        self.rules = TweetStreamRulesRequest(self)

    def __call__(self, max_retry_count=1, retry_wait_time=1):
        self.client._request_wait = 18
        search_mode = ['stream', 'sample'][0]
        kwargs = dict(
            search_mode=search_mode,
            max_retry_count=max_retry_count,
            retry_wait_time=retry_wait_time
        )
        return self._search(**kwargs)
