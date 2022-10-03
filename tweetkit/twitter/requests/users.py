"""All methods related to users."""
from tweetkit.twitter.exceptions import TwitterException, TwitterError, TwitterProblem
from tweetkit.twitter.response import Response

__all__ = [
    'Users'
]


class Users(object):
    """Endpoints related to retrieving, managing relationships of Users"""

    def __init__(self, client):
        self.client = client

    def list_get_followers(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                           tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/lists/{id}/followers', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def list_get_members(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                         tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/lists/{id}/members', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def tweets_id_liking_users(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                               tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-tweets-id-liking_users>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/tweets/{id}/liking_users', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def tweets_id_retweeting_users(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                                   tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweeted_by>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/tweets/{id}/retweeted_by', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def find_users_by_id(self, ids, user_fields=None, expansions=None, tweet_fields=None):
        """User lookup by IDs.

        This endpoint returns information about Users. Specify Users by their ID.

        Parameters
        ----------
        ids: list of string
            A list of User IDs, comma-separated. You can specify up to 100 IDs.Example: 2244994945,6253282,12.
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if ids is not None:
            query['ids'] = ids
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def find_users_by_username(self, usernames, user_fields=None, expansions=None, tweet_fields=None):
        """User lookup by usernames.

        This endpoint returns information about Users. Specify Users by their username.

        Parameters
        ----------
        usernames: list of string
            A list of usernames, comma-separated.
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if usernames is not None:
            query['usernames'] = usernames
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/by', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def find_user_by_username(self, username, user_fields=None, expansions=None, tweet_fields=None):
        """User lookup by username.

        This endpoint returns information about a User. Specify User by username.

        Parameters
        ----------
        username: string
            A username.Example: TwitterDev.
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if username is not None:
            params['username'] = username
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/by/username/{username}', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def find_my_user(self, user_fields=None, expansions=None, tweet_fields=None):
        """User lookup me.

        This endpoint returns information about the requesting User.

        Parameters
        ----------
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-me>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/me', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def find_user_by_id(self, id, user_fields=None, expansions=None, tweet_fields=None):
        """User lookup by ID.

        This endpoint returns information about a User. Specify User by ID.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/{id}', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_blocking(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                          tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/get-users-blocking>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/{id}/blocking', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_block(self, id):
        """Block User by User ID.

        Causes the User (in the path) to block the target User. The User (in the path) must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to block the target User.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/post-users-user_id-blocking>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        r = self.client.request('/2/users/{id}/blocking', method='post', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_followers(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                           tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/{id}/followers', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_following(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                           tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-following>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/{id}/following', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_follow(self, id):
        """Follow User.

        Causes the User(in the path) to follow, or “request to follow” for protected Users, the target User. The User(in the path) must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to follow the target User.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        r = self.client.request('/2/users/{id}/following', method='post', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_muting(self, id, max_results=None, pagination_token=None, user_fields=None, expansions=None,
                        tweet_fields=None):
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
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/get-users-muting>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        if max_results is not None:
            query['max_results'] = max_results
        if pagination_token is not None:
            query['pagination_token'] = pagination_token
        if user_fields is not None:
            query['user.fields'] = user_fields
        if expansions is not None:
            query['expansions'] = expansions
        if tweet_fields is not None:
            query['tweet.fields'] = tweet_fields
        r = self.client.request('/2/users/{id}/muting', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_mute(self, id):
        """Mute User by User ID.

        Causes the User (in the path) to mute the target User. The User (in the path) must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to mute the target User.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/post-users-user_id-muting>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if id is not None:
            params['id'] = id
        r = self.client.request('/2/users/{id}/muting', method='post', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_unblock(self, source_user_id, target_user_id):
        """Unblock User by User ID.

        Causes the source User to unblock the target User. The source User must match the User context authorizing the request.

        Parameters
        ----------
        source_user_id: string
            The ID of the authenticated source User that is requesting to unblock the target User.
        target_user_id: string
            The ID of the User that the source User is requesting to unblock.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/delete-users-user_id-blocking>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if source_user_id is not None:
            params['source_user_id'] = source_user_id
        if target_user_id is not None:
            params['target_user_id'] = target_user_id
        r = self.client.request('/2/users/{source_user_id}/blocking/{target_user_id}', method='delete', query=query,
                                params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_unfollow(self, source_user_id, target_user_id):
        """Unfollow User.

        Causes the source User to unfollow the target User. The source User must match the User context authorizing the request.

        Parameters
        ----------
        source_user_id: string
            The ID of the authenticated source User that is requesting to unfollow the target User.
        target_user_id: string
            The ID of the User that the source User is requesting to unfollow.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if source_user_id is not None:
            params['source_user_id'] = source_user_id
        if target_user_id is not None:
            params['target_user_id'] = target_user_id
        r = self.client.request('/2/users/{source_user_id}/following/{target_user_id}', method='delete', query=query,
                                params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()

    def users_id_unmute(self, source_user_id, target_user_id):
        """Unmute User by User ID.

        Causes the source User to unmute the target User. The source User must match the User context authorizing the request.

        Parameters
        ----------
        source_user_id: string
            The ID of the authenticated source User that is requesting to unmute the target User.
        target_user_id: string
            The ID of the User that the source User is requesting to unmute.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        if source_user_id is not None:
            params['source_user_id'] = source_user_id
        if target_user_id is not None:
            params['target_user_id'] = target_user_id
        r = self.client.request('/2/users/{source_user_id}/muting/{target_user_id}', method='delete', query=query,
                                params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request has succeeded.')
        else:
            if content_type == 'application/json':
                raise TwitterError(message='The request has failed.')
            if content_type == 'application/problem+json':
                raise TwitterProblem(message='The request has failed.')
        raise TwitterException()
