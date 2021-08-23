import time
import weakref

from six import string_types
from tweetkit.twitter.errors import TwitterException

__all__ = [
    'UserRequest',
    'TweetRequest',
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
        self.client = weakref.ref(client)

    @property
    def request(self):
        return self.client().request


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
        return TweetSearchOptions(self._search)

    def _search(self, query=None, **kwargs):
        """The recent search endpoint returns Tweets from the last seven days that match a search query.

        :param query: One rule for matching Tweets.
        :param kwargs: request options as dict
        :return:
        """
        search_mode = kwargs.pop('search_mode', 'recent')
        max_retry_count = kwargs.pop('max_retry_count', 3)
        retry_wait_time = kwargs.pop('retry_wait_time', 60)
        self.client().request_wait = 3
        if search_mode == 'recent':
            url = 'https://api.twitter.com/2/tweets/search/recent'
        else:
            url = 'https://api.twitter.com/2/tweets/search/all'
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
