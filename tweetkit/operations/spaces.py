"""All methods related to spaces."""
from tweetkit.exceptions import ProblemOrError, RequestException
from tweetkit.models import TwitterObject

__all__ = [
    'Spaces'
]


class Spaces(object):
    """Endpoints related to retrieving, managing Spaces"""

    def __init__(self, client):
        self.client = client

    def find_spaces_by_ids(self, ids, space_fields=None, expansions=None, user_fields=None, topic_fields=None):
        """Space lookup up Space IDs.

        Returns a variety of information about the Spaces specified by the requested IDs.

        Parameters
        ----------
        ids: list[string]
            The list of Space IDs to return.
        space_fields: list[string], optional
            A comma separated list of Space fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        topic_fields: list[string], optional
            A comma separated list of Topic fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['ids'] = ids
        if space_fields is not None:
            request_query['space.fields'] = space_fields
        else:
            request_params['space.fields'] = ['created_at', 'creator_id', 'ended_at', 'host_ids', 'id',
                                              'invited_user_ids', 'is_ticketed', 'lang', 'participant_count',
                                              'scheduled_start', 'speaker_ids', 'started_at', 'state',
                                              'subscriber_count', 'title', 'topic_ids', 'updated_at']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_params['expansions'] = ['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_params['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                             'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                             'url', 'username', 'verified', 'withheld']
        if topic_fields is not None:
            request_query['topic.fields'] = topic_fields
        else:
            request_params['topic.fields'] = ['description', 'id', 'name']
        r = self.client.request('/2/spaces', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                error = ProblemOrError(r)
                if error is not None:
                    raise error
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                problem = ProblemOrError(r)
                if problem is not None:
                    raise problem
        raise RequestException(r)

    def find_spaces_by_creator_ids(self, user_ids, space_fields=None, expansions=None, user_fields=None,
                                   topic_fields=None):
        """Space lookup by their creators.

        Returns a variety of information about the Spaces created by the provided User IDs.

        Parameters
        ----------
        user_ids: list[string]
            The IDs of Users to search through.
        space_fields: list[string], optional
            A comma separated list of Space fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        topic_fields: list[string], optional
            A comma separated list of Topic fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-by-creator-ids>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['user_ids'] = user_ids
        if space_fields is not None:
            request_query['space.fields'] = space_fields
        else:
            request_params['space.fields'] = ['created_at', 'creator_id', 'ended_at', 'host_ids', 'id',
                                              'invited_user_ids', 'is_ticketed', 'lang', 'participant_count',
                                              'scheduled_start', 'speaker_ids', 'started_at', 'state',
                                              'subscriber_count', 'title', 'topic_ids', 'updated_at']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_params['expansions'] = ['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_params['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                             'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                             'url', 'username', 'verified', 'withheld']
        if topic_fields is not None:
            request_query['topic.fields'] = topic_fields
        else:
            request_params['topic.fields'] = ['description', 'id', 'name']
        r = self.client.request('/2/spaces/by/creator_ids', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                error = ProblemOrError(r)
                if error is not None:
                    raise error
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                problem = ProblemOrError(r)
                if problem is not None:
                    raise problem
        raise RequestException(r)

    def search_spaces(self, query, state=None, max_results=None, space_fields=None, expansions=None, user_fields=None,
                      topic_fields=None):
        """Search for Spaces.

        Returns Spaces that match the provided query.

        Parameters
        ----------
        query: string
            The search query.Example: crypto.
        state: string, optional
            The state of Spaces to search for.
        max_results: integer, optional
            The number of results to return.
        space_fields: list[string], optional
            A comma separated list of Space fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        topic_fields: list[string], optional
            A comma separated list of Topic fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/spaces/search/api-reference/get-spaces-search>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['query'] = query
        if state is not None:
            request_query['state'] = state
        if max_results is not None:
            request_query['max_results'] = max_results
        if space_fields is not None:
            request_query['space.fields'] = space_fields
        else:
            request_params['space.fields'] = ['created_at', 'creator_id', 'ended_at', 'host_ids', 'id',
                                              'invited_user_ids', 'is_ticketed', 'lang', 'participant_count',
                                              'scheduled_start', 'speaker_ids', 'started_at', 'state',
                                              'subscriber_count', 'title', 'topic_ids', 'updated_at']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_params['expansions'] = ['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_params['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                             'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                             'url', 'username', 'verified', 'withheld']
        if topic_fields is not None:
            request_query['topic.fields'] = topic_fields
        else:
            request_params['topic.fields'] = ['description', 'id', 'name']
        r = self.client.request('/2/spaces/search', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                error = ProblemOrError(r)
                if error is not None:
                    raise error
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                problem = ProblemOrError(r)
                if problem is not None:
                    raise problem
        raise RequestException(r)

    def find_space_by_id(self, id, space_fields=None, expansions=None, user_fields=None, topic_fields=None):
        """Space lookup by Space ID.

        Returns a variety of information about the Space specified by the requested ID.

        Parameters
        ----------
        id: string
            The ID of the Space to be retrieved.Example: 1YqKDqWqdPLsV.
        space_fields: list[string], optional
            A comma separated list of Space fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        topic_fields: list[string], optional
            A comma separated list of Topic fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if space_fields is not None:
            request_query['space.fields'] = space_fields
        else:
            request_params['space.fields'] = ['created_at', 'creator_id', 'ended_at', 'host_ids', 'id',
                                              'invited_user_ids', 'is_ticketed', 'lang', 'participant_count',
                                              'scheduled_start', 'speaker_ids', 'started_at', 'state',
                                              'subscriber_count', 'title', 'topic_ids', 'updated_at']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_params['expansions'] = ['creator_id', 'host_ids', 'invited_user_ids', 'speaker_ids', 'topic_ids']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_params['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                             'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                             'url', 'username', 'verified', 'withheld']
        if topic_fields is not None:
            request_query['topic.fields'] = topic_fields
        else:
            request_params['topic.fields'] = ['description', 'id', 'name']
        r = self.client.request('/2/spaces/{id}', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                error = ProblemOrError(r)
                if error is not None:
                    raise error
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                problem = ProblemOrError(r)
                if problem is not None:
                    raise problem
        raise RequestException(r)

    def space_buyers(self, id, pagination_token=None, max_results=None, user_fields=None, expansions=None,
                     tweet_fields=None):
        """Retrieve the list of Users who purchased a ticket to the given space.

        Retrieves the list of Users who purchased a ticket to the given space.

        Parameters
        ----------
        id: string
            The ID of the Space to be retrieved.Example: 1YqKDqWqdPLsV.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        max_results: integer, optional
            The maximum number of results.
        user_fields: list[string], optional
            A comma separated list of User fields to display.
        expansions: list[string], optional
            A comma separated list of fields to expand.
        tweet_fields: list[string], optional
            A comma separated list of Tweet fields to display.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-buyers>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if max_results is not None:
            request_query['max_results'] = max_results
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_params['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                             'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                             'url', 'username', 'verified', 'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_params['expansions'] = ['pinned_tweet_id']
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_params['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                              'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities',
                                              'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics',
                                              'organic_metrics', 'possibly_sensitive', 'promoted_metrics',
                                              'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                              'withheld']
        r = self.client.request('/2/spaces/{id}/buyers', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                error = ProblemOrError(r)
                if error is not None:
                    raise error
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                problem = ProblemOrError(r)
                if problem is not None:
                    raise problem
        raise RequestException(r)

    def space_tweets(self, id, max_results=None, tweet_fields=None, expansions=None, media_fields=None,
                     poll_fields=None, user_fields=None, place_fields=None):
        """Retrieve Tweets from a Space.

        Retrieves Tweets shared in the specified Space.

        Parameters
        ----------
        id: string
            The ID of the Space to be retrieved.Example: 1YqKDqWqdPLsV.
        max_results: integer, optional
            The number of Tweets to fetch from the provided space. If not provided, the value will default to the maximum of 100.
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
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-tweets>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if max_results is not None:
            request_query['max_results'] = max_results
        if tweet_fields is not None:
            request_query['tweet.fields'] = tweet_fields
        else:
            request_params['tweet.fields'] = ['attachments', 'author_id', 'context_annotations', 'conversation_id',
                                              'created_at', 'edit_controls', 'edit_history_tweet_ids', 'entities',
                                              'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics',
                                              'organic_metrics', 'possibly_sensitive', 'promoted_metrics',
                                              'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text',
                                              'withheld']
        if expansions is not None:
            request_query['expansions'] = expansions
        else:
            request_params['expansions'] = ['attachments.media_keys', 'attachments.poll_ids', 'author_id',
                                            'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id',
                                            'in_reply_to_user_id', 'referenced_tweets.id',
                                            'referenced_tweets.id.author_id']
        if media_fields is not None:
            request_query['media.fields'] = media_fields
        else:
            request_params['media.fields'] = ['alt_text', 'duration_ms', 'height', 'media_key', 'non_public_metrics',
                                              'organic_metrics', 'preview_image_url', 'promoted_metrics',
                                              'public_metrics', 'type', 'url', 'variants', 'width']
        if poll_fields is not None:
            request_query['poll.fields'] = poll_fields
        else:
            request_params['poll.fields'] = ['duration_minutes', 'end_datetime', 'id', 'options', 'voting_status']
        if user_fields is not None:
            request_query['user.fields'] = user_fields
        else:
            request_params['user.fields'] = ['created_at', 'description', 'entities', 'id', 'location', 'name',
                                             'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics',
                                             'url', 'username', 'verified', 'withheld']
        if place_fields is not None:
            request_query['place.fields'] = place_fields
        else:
            request_params['place.fields'] = ['contained_within', 'country', 'country_code', 'full_name', 'geo', 'id',
                                              'name', 'place_type']
        r = self.client.request('/2/spaces/{id}/tweets', method='get', query=request_query, params=request_params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has succeeded.
                return TwitterObject(r)
        else:
            if content_type is not None and content_type.startswith('application/json'):
                # The request has failed.
                error = ProblemOrError(r)
                if error is not None:
                    raise error
            if content_type is not None and content_type.startswith('application/problem+json'):
                # The request has failed.
                problem = ProblemOrError(r)
                if problem is not None:
                    raise problem
        raise RequestException(r)
