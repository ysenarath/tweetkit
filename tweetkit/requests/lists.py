"""All methods related to lists."""
from tweetkit.models import Paginator, TwitterStreamResponse, TwitterResponse

__all__ = [
    'Lists'
]


class Lists(object):
    """Endpoints related to retrieving, managing Lists"""

    def __init__(self, client):
        self.client = client

    def list_id_create(self, data=None, **kwargs):
        """Create List.

        Creates a new List.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/post-lists>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        return self.client.request('/2/lists', method='post', query=request_query, params=request_params, data=data,
                                   dtype='data', **kwargs)

    def list_id_delete(self, id, data=None, **kwargs):
        """Delete List.

        Delete a List that you own.

        Parameters
        ----------
        id: string
            The ID of the List to delete.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/delete-lists-id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/lists/{id}', method='delete', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def list_id_get(self, id, list_fields=None, expansions=None, user_fields=None, data=None, **kwargs):
        """List lookup by List ID.

        Returns a List.

        Parameters
        ----------
        id: string
            The ID of the List.
        list_fields: list[string], optional
            A comma separated list of List fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-lists-id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        else:
            request_query['list.fields'] = ['created_at', 'description', 'follower_count', 'id', 'member_count', 'name',
                                            'owner_id', 'private']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['owner_id']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        return self.client.request('/2/lists/{id}', method='get', query=request_query, params=request_params, data=data,
                                   dtype='List', **kwargs)

    def list_id_update(self, id, data=None, **kwargs):
        """Update List.

        Update a List that you own.

        Parameters
        ----------
        id: string
            The ID of the List to modify.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/put-lists-id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/lists/{id}', method='put', query=request_query, params=request_params, data=data,
                                   dtype='data', **kwargs)

    def list_add_member(self, id, data=None, **kwargs):
        """Add a List member.

        Causes a User to become a member of a List.

        Parameters
        ----------
        id: string
            The ID of the List for which to add a member.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/post-lists-id-members>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/lists/{id}/members', method='post', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def list_remove_member(self, id, user_id, data=None, **kwargs):
        """Remove a List member.

        Causes a User to be removed from the members of a List.

        Parameters
        ----------
        id: string
            The ID of the List to remove a member.
        user_id: string
            The ID of User that will be removed from the List.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/delete-lists-id-members-user_id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['user_id'] = user_id
        return self.client.request('/2/lists/{id}/members/{user_id}', method='delete', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)

    def user_followed_lists(self, id, max_results=None, pagination_token=None, list_fields=None, expansions=None,
                            user_fields=None, data=None, **kwargs):
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
        list_fields: list[string], optional
            A comma separated list of List fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/get-users-id-followed_lists>`__.
        
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
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        else:
            request_query['list.fields'] = ['created_at', 'description', 'follower_count', 'id', 'member_count', 'name',
                                            'owner_id', 'private']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['owner_id']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        return self.client.request('/2/users/{id}/followed_lists', method='get', query=request_query,
                                   params=request_params, data=data, dtype='List', **kwargs)

    def list_user_follow(self, id, data=None, **kwargs):
        """Follow a List.

        Causes a User to follow a List.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that will follow the List.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/post-users-id-followed-lists>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/followed_lists', method='post', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)

    def list_user_unfollow(self, id, list_id, data=None, **kwargs):
        """Unfollow a List.

        Causes a User to unfollow a List.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that will unfollow the List.
        list_id: string
            The ID of the List to unfollow.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/delete-users-id-followed-lists-list_id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['list_id'] = list_id
        return self.client.request('/2/users/{id}/followed_lists/{list_id}', method='delete', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)

    def get_user_list_memberships(self, id, max_results=None, pagination_token=None, list_fields=None, expansions=None,
                                  user_fields=None, data=None, **kwargs):
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
        list_fields: list[string], optional
            A comma separated list of List fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
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
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        else:
            request_query['list.fields'] = ['created_at', 'description', 'follower_count', 'id', 'member_count', 'name',
                                            'owner_id', 'private']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['owner_id']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        return self.client.request('/2/users/{id}/list_memberships', method='get', query=request_query,
                                   params=request_params, data=data, dtype='List', **kwargs)

    def list_user_owned_lists(self, id, max_results=None, pagination_token=None, list_fields=None, expansions=None,
                              user_fields=None, data=None, **kwargs):
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
        list_fields: list[string], optional
            A comma separated list of List fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists>`__.
        
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
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        else:
            request_query['list.fields'] = ['created_at', 'description', 'follower_count', 'id', 'member_count', 'name',
                                            'owner_id', 'private']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['owner_id']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        return self.client.request('/2/users/{id}/owned_lists', method='get', query=request_query,
                                   params=request_params, data=data, dtype='List', **kwargs)

    def list_user_pinned_lists(self, id, list_fields=None, expansions=None, user_fields=None, data=None, **kwargs):
        """Get a User's Pinned Lists.

        Get a User's Pinned Lists.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to return results.
        list_fields: list[string], optional
            A comma separated list of List fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/get-users-id-pinned_lists>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if list_fields is not None:
            request_query['list.fields'] = list_fields
        else:
            request_query['list.fields'] = ['created_at', 'description', 'follower_count', 'id', 'member_count', 'name',
                                            'owner_id', 'private']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['owner_id']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        return self.client.request('/2/users/{id}/pinned_lists', method='get', query=request_query,
                                   params=request_params, data=data, dtype='List', **kwargs)

    def list_user_pin(self, data, id, **kwargs):
        """Pin a List.

        Causes a User to pin a List.

        Parameters
        ----------
        data: dict
            The request body.
        id: string
            The ID of the authenticated source User that will pin the List.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/post-users-id-pinned-lists>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/pinned_lists', method='post', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)

    def list_user_unpin(self, id, list_id, data=None, **kwargs):
        """Unpin a List.

        Causes a User to remove a pinned List.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to return results.
        list_id: string
            The ID of the List to unpin.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/delete-users-id-pinned-lists-list_id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['list_id'] = list_id
        return self.client.request('/2/users/{id}/pinned_lists/{list_id}', method='delete', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)
