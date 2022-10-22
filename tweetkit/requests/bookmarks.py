"""All methods related to bookmarks."""
from tweetkit.models import Paginator, TwitterStreamResponse, TwitterResponse

__all__ = [
    'Bookmarks'
]


class Bookmarks(object):
    """Endpoints related to retrieving, managing bookmarks of a user"""

    def __init__(self, client):
        self.client = client

    def get_users_id_bookmarks(self, id, max_results=None, pagination_token=None, tweet_fields=None, expansions=None,
                               media_fields=None, poll_fields=None, user_fields=None, place_fields=None, data=None,
                               **kwargs):
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
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        media_fields: list[string], optional
            A comma separated list of Media fields to display.
        poll_fields: list[string], optional
            A comma separated list of Poll fields to display.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        place_fields: list[string], optional
            A comma separated list of Place fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/get-users-id-bookmarks>`__.
        
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
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_query['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                             'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo',
                                             'id', 'in_reply_to_user_id', 'lang', 'possibly_sensitive',
                                             'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                             'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_query['expansions'] = ['attachments.media_keys', 'attachments.poll_ids', 'author_id',
                                           'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id',
                                           'in_reply_to_user_id', 'referenced_tweets.id',
                                           'referenced_tweets.id.author_id']
        if media_fields is not None:
            request_query['media.fields'] = media_fields
        else:
            request_query['media.fields'] = ['alt_text', 'duration_ms', 'height', 'media_key', 'preview_image_url',
                                             'public_metrics', 'type', 'url', 'variants', 'width']
        if poll_fields is not None:
            request_query['poll.fields'] = poll_fields
        else:
            request_query['poll.fields'] = ['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_query['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                            'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                            'url', 'username', 'verified', 'withheld']
        if place_fields is not None:
            request_query['place.fields'] = place_fields
        else:
            request_query['place.fields'] = ['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id',
                                             'name', 'place_type']
        return self.client.request('/2/users/{id}/bookmarks', method='get', query=request_query, params=request_params,
                                   data=data, dtype='Tweet', **kwargs)

    def post_users_id_bookmarks(self, data, id, **kwargs):
        """Add Tweet to Bookmarks.

        Adds a Tweet (ID in the body) to the requesting User's (in the path) bookmarks.

        Parameters
        ----------
        data: dict
            The request body.
        id: string
            The ID of the authenticated source User for whom to add bookmarks.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/post-users-id-bookmarks>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/bookmarks', method='post', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def users_id_bookmarks_delete(self, id, tweet_id, data=None, **kwargs):
        """Remove a bookmarked Tweet.

        Removes a Tweet from the requesting User's bookmarked Tweets.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User whose bookmark is to be removed.
        tweet_id: string
            The ID of the Tweet that the source User is removing from bookmarks.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/delete-users-id-bookmarks-tweet_id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['tweet_id'] = tweet_id
        return self.client.request('/2/users/{id}/bookmarks/{tweet_id}', method='delete', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)
