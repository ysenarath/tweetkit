"""All methods related to bookmarks."""
from tweetkit.exceptions import TwitterError, TwitterProblem, RequestException
from tweetkit.schema import TwitterObject

__all__ = [
    'Bookmarks'
]


class Bookmarks(object):
    """Endpoints related to retrieving, managing bookmarks of a user"""

    def __init__(self, client):
        self.client = client

    def get_users_id_bookmarks(self, id, max_results=None, pagination_token=None, tweet_fields=None, expansions=None,
                               media_fields=None, poll_fields=None, user_fields=None, place_fields=None):
        """Bookmarks by User.

        Returns Tweet objects that have been bookmarked by the requesting User.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to return results.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results.
        tweet_fields: list of string, optional
            A comma separated list of Tweet fields to display.
        expansions: list of string, optional
            A comma separated list of fields to expand.
        media_fields: list of string, optional
            A comma separated list of Media fields to display.
        poll_fields: list of string, optional
            A comma separated list of Poll fields to display.
        user_fields: list of string, optional
            A comma separated list of User fields to display.
        place_fields: list of string, optional
            A comma separated list of Place fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/get-users-id-bookmarks>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        if expansions is not None:
            request_query['expansions'] = expansions
        if media_fields is not None:
            request_query['media.fields'] = media_fields
        if poll_fields is not None:
            request_query['poll.fields'] = poll_fields
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        if place_fields is not None:
            request_query['place.fields'] = place_fields
        r = self.client.request('/2/users/{id}/bookmarks', method='get', query=request_query, params=request_params)
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

    def post_users_id_bookmarks(self, id):
        """Add Tweet to Bookmarks.

        Adds a Tweet (ID in the body) to the requesting User's (in the path) bookmarks.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User for whom to add bookmarks.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/post-users-id-bookmarks>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        r = self.client.request('/2/users/{id}/bookmarks', method='post', query=request_query, params=request_params)
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

    def users_id_bookmarks_delete(self, id, tweet_id):
        """Remove a bookmarked Tweet.

        Removes a Tweet from the requesting User's bookmarked Tweets.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User whose bookmark is to be removed.
        tweet_id: string
            The ID of the Tweet that the source User is removing from bookmarks.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/delete-users-id-bookmarks-tweet_id>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['tweet_id'] = tweet_id
        r = self.client.request('/2/users/{id}/bookmarks/{tweet_id}', method='delete', query=request_query,
                                params=request_params)
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
