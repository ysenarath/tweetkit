"""All methods related to lists."""
from tweetkit.exceptions import TwitterError, TwitterProblem, RequestException
from tweetkit.schema import TwitterObject, TwitterObjectStream

__all__ = [
    'Lists'
]


class Lists(object):
    """Endpoints related to retrieving, managing Lists"""
    
    def __init__(self, client):
        self.client = client

    def list_id_create(self):
        """Create List.

        Creates a new List.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/post-lists>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        r = self.client.request('/2/lists', method='post', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_id_delete(self, id):
        """Delete List.

        Delete a List that you own.

        Parameters
        ----------
        id: string
            The ID of the List to delete.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/delete-lists-id>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        r = self.client.request('/2/lists/{id}', method='delete', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_id_get(self, id, list_fields=None, expansions=None, user_fields=None):
        """List lookup by List ID.

        Returns a List.

        Parameters
        ----------
        id: string
            The ID of the List.
        list_fields: list of {'created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private'}, optional
            A comma separated list of List fields to display.
        expansions: list of {'owner_id'}, optional
            A comma separated list of fields to expand.
        user_fields: list of {'created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'}, optional
            A comma separated list of User fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-lists-id>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        if expansions is not None:
            request_query['expansions'] = expansions
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        r = self.client.request('/2/lists/{id}', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_id_update(self, id):
        """Update List.

        Update a List that you own.

        Parameters
        ----------
        id: string
            The ID of the List to modify.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/put-lists-id>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        r = self.client.request('/2/lists/{id}', method='put', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_add_member(self, id):
        """Add a List member.

        Causes a User to become a member of a List.

        Parameters
        ----------
        id: string
            The ID of the List for which to add a member.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/post-lists-id-members>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        r = self.client.request('/2/lists/{id}/members', method='post', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_remove_member(self, id, user_id):
        """Remove a List member.

        Causes a User to be removed from the members of a List.

        Parameters
        ----------
        id: string
            The ID of the List to remove a member.
        user_id: string
            The ID of User that will be removed from the List.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/delete-lists-id-members-user_id>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['user_id'] = user_id
        r = self.client.request('/2/lists/{id}/members/{user_id}', method='delete', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def user_followed_lists(self, id, max_results=None, pagination_token=None, list_fields=None, expansions=None, user_fields=None):
        """Get User's Followed Lists.

        Returns a User's followed Lists.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        list_fields: list of {'created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private'}, optional
            A comma separated list of List fields to display.
        expansions: list of {'owner_id'}, optional
            A comma separated list of fields to expand.
        user_fields: list of {'created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'}, optional
            A comma separated list of User fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/get-users-id-followed_lists>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        if expansions is not None:
            request_query['expansions'] = expansions
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        r = self.client.request('/2/users/{id}/followed_lists', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_user_follow(self, id):
        """Follow a List.

        Causes a User to follow a List.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that will follow the List.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/post-users-id-followed-lists>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        r = self.client.request('/2/users/{id}/followed_lists', method='post', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_user_unfollow(self, id, list_id):
        """Unfollow a List.

        Causes a User to unfollow a List.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that will unfollow the List.
        list_id: string
            The ID of the List to unfollow.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/delete-users-id-followed-lists-list_id>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['list_id'] = list_id
        r = self.client.request('/2/users/{id}/followed_lists/{list_id}', method='delete', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def get_user_list_memberships(self, id, max_results=None, pagination_token=None, list_fields=None, expansions=None, user_fields=None):
        """Get a User's List Memberships.

        Get a User's List Memberships.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        list_fields: list of {'created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private'}, optional
            A comma separated list of List fields to display.
        expansions: list of {'owner_id'}, optional
            A comma separated list of fields to expand.
        user_fields: list of {'created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'}, optional
            A comma separated list of User fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        if expansions is not None:
            request_query['expansions'] = expansions
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        r = self.client.request('/2/users/{id}/list_memberships', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_user_owned_lists(self, id, max_results=None, pagination_token=None, list_fields=None, expansions=None, user_fields=None):
        """Get a User's Owned Lists.

        Get a User's Owned Lists.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        list_fields: list of {'created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private'}, optional
            A comma separated list of List fields to display.
        expansions: list of {'owner_id'}, optional
            A comma separated list of fields to expand.
        user_fields: list of {'created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'}, optional
            A comma separated list of User fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        if expansions is not None:
            request_query['expansions'] = expansions
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        r = self.client.request('/2/users/{id}/owned_lists', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_user_pinned_lists(self, id, list_fields=None, expansions=None, user_fields=None):
        """Get a User's Pinned Lists.

        Get a User's Pinned Lists.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to return results.
        list_fields: list of {'created_at', 'description', 'follower_count', 'id', 'member_count', 'name', 'owner_id', 'private'}, optional
            A comma separated list of List fields to display.
        expansions: list of {'owner_id'}, optional
            A comma separated list of fields to expand.
        user_fields: list of {'created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'}, optional
            A comma separated list of User fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/get-users-id-pinned_lists>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        if expansions is not None:
            request_query['expansions'] = expansions
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        r = self.client.request('/2/users/{id}/pinned_lists', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_user_pin(self, id):
        """Pin a List.

        Causes a User to pin a List.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that will pin the List.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/post-users-id-pinned-lists>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        r = self.client.request('/2/users/{id}/pinned_lists', method='post', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)

    def list_user_unpin(self, id, list_id):
        """Unpin a List.

        Causes a User to remove a pinned List.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to return results.
        list_id: string
            The ID of the List to unpin.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/delete-users-id-pinned-lists-list_id>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['list_id'] = list_id
        r = self.client.request('/2/users/{id}/pinned_lists/{list_id}', method='delete', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                raise TwitterError(r)
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                raise TwitterProblem(r)
        raise RequestException(r)
