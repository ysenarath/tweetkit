"""All methods related to users."""
from tweetkit.models import Paginator, TwitterStreamResponse, TwitterResponse

__all__ = [
    'Users'
]


class Users(object):
    """Endpoints related to retrieving, managing relationships of Users"""

    def __init__(self, client):
        self.client = client

    def list_get_followers(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                           tweet_fields=None, data=None, **kwargs):
        """Returns User objects that follow a List by the provided List ID.

        Returns a list of Users that follow a List by the provided List ID.

        Parameters
        ----------
        id: string
            The ID of the List.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/lists/{id}/followers', method='get', query=request_query, params=request_params,
                                   data=data, dtype='User', **kwargs)

    def list_get_members(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                         tweet_fields=None, data=None, **kwargs):
        """Returns User objects that are members of a List by the provided List ID.

        Returns a list of Users that are members of a List by the provided List ID.

        Parameters
        ----------
        id: string
            The ID of the List.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/lists/{id}/members', method='get', query=request_query, params=request_params,
                                   data=data, dtype='User', **kwargs)

    def tweets_id_liking_users(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                               tweet_fields=None, data=None, **kwargs):
        """Returns User objects that have liked the provided Tweet ID.

        Returns a list of Users that have liked the provided Tweet ID.

        Parameters
        ----------
        id: string
            A single Tweet ID.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-tweets-id-liking_users>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/tweets/{id}/liking_users', method='get', query=request_query,
                                   params=request_params, data=data, dtype='User', **kwargs)

    def tweets_id_retweeting_users(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                                   tweet_fields=None, data=None, **kwargs):
        """Returns User objects that have retweeted the provided Tweet ID.

        Returns a list of Users that have retweeted the provided Tweet ID.

        Parameters
        ----------
        id: string
            A single Tweet ID.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweeted_by>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/tweets/{id}/retweeted_by', method='get', query=request_query,
                                   params=request_params, data=data, dtype='User', **kwargs)

    def find_users_by_id(self, ids, user_fields=None, expansions=None, tweet_fields=None, data=None, **kwargs):
        """User lookup by IDs.

        This endpoint returns information about Users. Specify Users by their ID.

        Parameters
        ----------
        ids: list[string]
            A list of User IDs, comma-separated. You can specify up to 100 IDs.Example: 2244994945,6253282,12.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['ids'] = ids
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users', method='get', query=request_query, params=request_params, data=data,
                                   dtype='User', **kwargs)

    def find_users_by_username(self, usernames, user_fields=None, expansions=None, tweet_fields=None, data=None,
                               **kwargs):
        """User lookup by usernames.

        This endpoint returns information about Users. Specify Users by their username.

        Parameters
        ----------
        usernames: list[string]
            A list of usernames, comma-separated.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['usernames'] = usernames
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/by', method='get', query=request_query, params=request_params, data=data,
                                   dtype='User', **kwargs)

    def find_user_by_username(self, username, user_fields=None, expansions=None, tweet_fields=None, data=None,
                              **kwargs):
        """User lookup by username.

        This endpoint returns information about a User. Specify User by username.

        Parameters
        ----------
        username: string
            A username.Example: TwitterDev.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['username'] = username
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/by/username/{username}', method='get', query=request_query,
                                   params=request_params, data=data, dtype='User', **kwargs)

    def find_my_user(self, user_fields=None, expansions=None, tweet_fields=None, data=None, **kwargs):
        """User lookup me.

        This endpoint returns information about the requesting User.

        Parameters
        ----------
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-me>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/me', method='get', query=request_query, params=request_params, data=data,
                                   dtype='User', **kwargs)

    def find_user_by_id(self, id, user_fields=None, expansions=None, tweet_fields=None, data=None, **kwargs):
        """User lookup by ID.

        This endpoint returns information about a User. Specify User by ID.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/{id}', method='get', query=request_query, params=request_params, data=data,
                                   dtype='User', **kwargs)

    def users_id_blocking(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                          tweet_fields=None, data=None, **kwargs):
        """Returns User objects that are blocked by provided User ID.

        Returns a list of Users that are blocked by the provided User ID.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to return results.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/get-users-blocking>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/{id}/blocking', method='get', query=request_query, params=request_params,
                                   data=data, dtype='User', **kwargs)

    def users_id_block(self, data, id, **kwargs):
        """Block User by User ID.

        Causes the User (in the path) to block the target User. The User (in the path) must match the User context authorizing the request.

        Parameters
        ----------
        data: dict
            The request body.
        id: string
            The ID of the authenticated source User that is requesting to block the target User.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/post-users-user_id-blocking>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/blocking', method='post', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def users_id_followers(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                           tweet_fields=None, data=None, **kwargs):
        """Followers by User ID.

        Returns a list of Users who are followers of the specified User ID.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/{id}/followers', method='get', query=request_query, params=request_params,
                                   data=data, dtype='User', **kwargs)

    def users_id_following(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                           tweet_fields=None, data=None, **kwargs):
        """Following by User ID.

        Returns a list of Users that are being followed by the provided User ID.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-following>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/{id}/following', method='get', query=request_query, params=request_params,
                                   data=data, dtype='User', **kwargs)

    def users_id_follow(self, id, data=None, **kwargs):
        """Follow User.

        Causes the User(in the path) to follow, or “request to follow” for protected Users, the target User. The User(in the path) must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to follow the target User.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/following', method='post', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def users_id_muting(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                        tweet_fields=None, data=None, **kwargs):
        """Returns User objects that are muted by the provided User ID.

        Returns a list of Users that are muted by the provided User ID.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to return results.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/get-users-muting>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        return self.client.request('/2/users/{id}/muting', method='get', query=request_query, params=request_params,
                                   data=data, dtype='User', **kwargs)

    def users_id_mute(self, id, data=None, **kwargs):
        """Mute User by User ID.

        Causes the User (in the path) to mute the target User. The User (in the path) must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to mute the target User.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/post-users-user_id-muting>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/muting', method='post', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def users_id_unblock(self, source_user_id, target_user_id, data=None, **kwargs):
        """Unblock User by User ID.

        Causes the source User to unblock the target User. The source User must match the User context authorizing the request.

        Parameters
        ----------
        source_user_id: string
            The ID of the authenticated source User that is requesting to unblock the target User.
        target_user_id: string
            The ID of the User that the source User is requesting to unblock.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/delete-users-user_id-blocking>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['source_user_id'] = source_user_id
        request_params['target_user_id'] = target_user_id
        return self.client.request('/2/users/{source_user_id}/blocking/{target_user_id}', method='delete',
                                   query=request_query, params=request_params, data=data, dtype='data', **kwargs)

    def users_id_unfollow(self, source_user_id, target_user_id, data=None, **kwargs):
        """Unfollow User.

        Causes the source User to unfollow the target User. The source User must match the User context authorizing the request.

        Parameters
        ----------
        source_user_id: string
            The ID of the authenticated source User that is requesting to unfollow the target User.
        target_user_id: string
            The ID of the User that the source User is requesting to unfollow.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['source_user_id'] = source_user_id
        request_params['target_user_id'] = target_user_id
        return self.client.request('/2/users/{source_user_id}/following/{target_user_id}', method='delete',
                                   query=request_query, params=request_params, data=data, dtype='data', **kwargs)

    def users_id_unmute(self, source_user_id, target_user_id, data=None, **kwargs):
        """Unmute User by User ID.

        Causes the source User to unmute the target User. The source User must match the User context authorizing the request.

        Parameters
        ----------
        source_user_id: string
            The ID of the authenticated source User that is requesting to unmute the target User.
        target_user_id: string
            The ID of the User that the source User is requesting to unmute.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['source_user_id'] = source_user_id
        request_params['target_user_id'] = target_user_id
        return self.client.request('/2/users/{source_user_id}/muting/{target_user_id}', method='delete',
                                   query=request_query, params=request_params, data=data, dtype='data', **kwargs)
