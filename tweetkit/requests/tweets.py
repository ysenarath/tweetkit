"""All methods related to tweets."""
from tweetkit.models import Paginator, TwitterStreamResponse, TwitterResponse

__all__ = [
    'Tweets'
]


class Tweets(object):
    """Endpoints related to retrieving, searching, and modifying Tweets"""

    def __init__(self, client):
        self.client = client

    def lists_id_tweets(self, id, max_results=None, pagination_token=None, tweet_fields=None, expansions=None,
                        media_fields=None, poll_fields=None, user_fields=None, place_fields=None, data=None, **kwargs):
        """List Tweets timeline by List ID.

        Returns a list of Tweets associated with the provided List ID.

        Parameters
        ----------
        id: string
            The ID of the List.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference/get-lists-id-tweets>`__.
        
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
        return self.client.request('/2/lists/{id}/tweets', method='get', query=request_query, params=request_params,
                                   data=data, dtype='Tweet', **kwargs)

    def find_tweets_by_id(self, ids, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None,
                          user_fields=None, place_fields=None, data=None, **kwargs):
        """Tweet lookup by Tweet IDs.

        Returns a variety of information about the Tweet specified by the requested ID.

        Parameters
        ----------
        ids: list[string]
            A comma separated list of Tweet IDs. Up to 100 are allowed in a single request.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['ids'] = ids
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
        return self.client.request('/2/tweets', method='get', query=request_query, params=request_params, data=data,
                                   dtype='Tweet', **kwargs)

    def create_tweet(self, data, **kwargs):
        """Creation of a Tweet.

        Causes the User to create a Tweet under the authorized account.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        return self.client.request('/2/tweets', method='post', query=request_query, params=request_params, data=data,
                                   dtype='data', **kwargs)

    def tweet_counts_full_archive_search(self, query, start_time=None, end_time=None, since_id=None, until_id=None,
                                         next_token=None, pagination_token=None, granularity=None,
                                         search_count_fields=None, data=None, **kwargs):
        """Full archive search counts.

        Returns Tweet Counts that match a search query.

        Parameters
        ----------
        query: string
            One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        since_id: string, optional
            Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
        until_id: string, optional
            Returns results with a Tweet ID less than (that is, older than) the specified ID.
        next_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        granularity: string, optional
            The granularity for the search counts results.
        search_count_fields: list[string], optional
            A comma separated list of SearchCount fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['query'] = query
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
        if since_id is not None:
            request_query['since_id'] = since_id
        if until_id is not None:
            request_query['until_id'] = until_id
        if next_token is not None:
            request_query['next_token'] = next_token
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if granularity is not None:
            request_query['granularity'] = granularity
        if search_count_fields is not None:
            request_query['search_count.fields'] = search_count_fields
        else:
            request_query['search_count.fields'] = ['end', 'start', 'tweet_count']
        return self.client.request('/2/tweets/counts/all', method='get', query=request_query, params=request_params,
                                   data=data, dtype='SearchCount', **kwargs)

    def tweet_counts_recent_search(self, query, start_time=None, end_time=None, since_id=None, until_id=None,
                                   next_token=None, pagination_token=None, granularity=None, search_count_fields=None,
                                   data=None, **kwargs):
        """Recent search counts.

        Returns Tweet Counts from the last 7 days that match a search query.

        Parameters
        ----------
        query: string
            One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        since_id: string, optional
            Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
        until_id: string, optional
            Returns results with a Tweet ID less than (that is, older than) the specified ID.
        next_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        granularity: string, optional
            The granularity for the search counts results.
        search_count_fields: list[string], optional
            A comma separated list of SearchCount fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['query'] = query
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
        if since_id is not None:
            request_query['since_id'] = since_id
        if until_id is not None:
            request_query['until_id'] = until_id
        if next_token is not None:
            request_query['next_token'] = next_token
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if granularity is not None:
            request_query['granularity'] = granularity
        if search_count_fields is not None:
            request_query['search_count.fields'] = search_count_fields
        else:
            request_query['search_count.fields'] = ['end', 'start', 'tweet_count']
        return self.client.request('/2/tweets/counts/recent', method='get', query=request_query, params=request_params,
                                   data=data, dtype='SearchCount', **kwargs)

    def get_tweets_firehose_stream(self, partition, backfill_minutes=None, start_time=None, end_time=None,
                                   tweet_fields=None, expansions=None, media_fields=None, poll_fields=None,
                                   user_fields=None, place_fields=None, data=None, **kwargs):
        """Firehose stream.

        Streams 100% of public Tweets.

        Parameters
        ----------
        partition: integer
            The partition number.
        backfill_minutes: integer, optional
            The number of minutes of backfill requested.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.Example: 2021-02-14T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.Example: 2021-02-14T18:40:40.000Z.
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
        For more information, see: `here <None>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['partition'] = partition
        if backfill_minutes is not None:
            request_query['backfill_minutes'] = backfill_minutes
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
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
        return self.client.request('/2/tweets/firehose/stream', method='get', query=request_query,
                                   params=request_params, data=data, stream=True, dtype='Tweet', **kwargs)

    def sample_stream(self, backfill_minutes=None, tweet_fields=None, expansions=None, media_fields=None,
                      poll_fields=None, user_fields=None, place_fields=None, data=None, **kwargs):
        """Sample stream.

        Streams a deterministic 1% of public Tweets.

        Parameters
        ----------
        backfill_minutes: integer, optional
            The number of minutes of backfill requested.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/api-reference/get-tweets-sample-stream>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        if backfill_minutes is not None:
            request_query['backfill_minutes'] = backfill_minutes
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
        return self.client.request('/2/tweets/sample/stream', method='get', query=request_query, params=request_params,
                                   data=data, stream=True, dtype='Tweet', **kwargs)

    def get_tweets_sample10_stream(self, partition, backfill_minutes=None, start_time=None, end_time=None,
                                   tweet_fields=None, expansions=None, media_fields=None, poll_fields=None,
                                   user_fields=None, place_fields=None, data=None, **kwargs):
        """Sample 10% stream.

        Streams a deterministic 10% of public Tweets.

        Parameters
        ----------
        partition: integer
            The partition number.
        backfill_minutes: integer, optional
            The number of minutes of backfill requested.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.Example: 2021-02-14T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.Example: 2021-02-14T18:40:40.000Z.
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
        For more information, see: `here <None>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['partition'] = partition
        if backfill_minutes is not None:
            request_query['backfill_minutes'] = backfill_minutes
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
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
        return self.client.request('/2/tweets/sample10/stream', method='get', query=request_query,
                                   params=request_params, data=data, stream=True, dtype='Tweet', **kwargs)

    def tweets_fullarchive_search(self, query, start_time=None, end_time=None, since_id=None, until_id=None,
                                  max_results=None, next_token=None, pagination_token=None, sort_order=None,
                                  tweet_fields=None, expansions=None, media_fields=None, poll_fields=None,
                                  user_fields=None, place_fields=None, data=None, **kwargs):
        """Full-archive search.

        Returns Tweets that match a search query.

        Parameters
        ----------
        query: string
            One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        since_id: string, optional
            Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
        until_id: string, optional
            Returns results with a Tweet ID less than (that is, older than) the specified ID.
        max_results: integer, optional
            The maximum number of search results to be returned by a request.
        next_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        sort_order: string, optional
            This order in which to return results.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['query'] = query
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
        if since_id is not None:
            request_query['since_id'] = since_id
        if until_id is not None:
            request_query['until_id'] = until_id
        if max_results is not None:
            request_query['max_results'] = max_results
        if next_token is not None:
            request_query['next_token'] = next_token
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if sort_order is not None:
            request_query['sort_order'] = sort_order
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
        return self.client.request('/2/tweets/search/all', method='get', query=request_query, params=request_params,
                                   data=data, dtype='Tweet', **kwargs)

    def tweets_recent_search(self, query, start_time=None, end_time=None, since_id=None, until_id=None,
                             max_results=None, next_token=None, pagination_token=None, sort_order=None,
                             tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None,
                             place_fields=None, data=None, **kwargs):
        """Recent search.

        Returns Tweets from the last 7 days that match a search query.

        Parameters
        ----------
        query: string
            One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        since_id: string, optional
            Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
        until_id: string, optional
            Returns results with a Tweet ID less than (that is, older than) the specified ID.
        max_results: integer, optional
            The maximum number of search results to be returned by a request.
        next_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        sort_order: string, optional
            This order in which to return results.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['query'] = query
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
        if since_id is not None:
            request_query['since_id'] = since_id
        if until_id is not None:
            request_query['until_id'] = until_id
        if max_results is not None:
            request_query['max_results'] = max_results
        if next_token is not None:
            request_query['next_token'] = next_token
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if sort_order is not None:
            request_query['sort_order'] = sort_order
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
        return self.client.request('/2/tweets/search/recent', method='get', query=request_query, params=request_params,
                                   data=data, dtype='Tweet', **kwargs)

    def search_stream(self, backfill_minutes=None, start_time=None, end_time=None, tweet_fields=None, expansions=None,
                      media_fields=None, poll_fields=None, user_fields=None, place_fields=None, data=None, **kwargs):
        """Filtered stream.

        Streams Tweets matching the stream's active rule set.

        Parameters
        ----------
        backfill_minutes: integer, optional
            The number of minutes of backfill requested.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided.Example: 2021-02-01T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.Example: 2021-02-14T18:40:40.000Z.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        if backfill_minutes is not None:
            request_query['backfill_minutes'] = backfill_minutes
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
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
        return self.client.request('/2/tweets/search/stream', method='get', query=request_query, params=request_params,
                                   data=data, stream=True, dtype='Tweet', **kwargs)

    def get_rules(self, ids=None, max_results=None, pagination_token=None, data=None, **kwargs):
        """Rules lookup.

        Returns rules from a User's active rule set. Users can fetch all of their rules or a subset, specified by the provided rule ids.

        Parameters
        ----------
        ids: list[string], optional
            A comma-separated list of Rule IDs.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This value is populated by passing the 'next_token' returned in a request to paginate through results.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        if ids is not None:
            request_query['ids'] = ids
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        return self.client.request('/2/tweets/search/stream/rules', method='get', query=request_query,
                                   params=request_params, data=data, dtype='Rule', **kwargs)

    def add_or_delete_rules(self, data, dry_run=None, **kwargs):
        """Add/Delete rules.

        Add or delete rules from a User's active rule set. Users can provide unique, optionally tagged rules to add. Users can delete their entire rule set or a subset specified by rule ids or values.

        Parameters
        ----------
        data: dict
            The request body.
        dry_run: boolean, optional
            Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        if dry_run is not None:
            request_query['dry_run'] = dry_run
        return self.client.request('/2/tweets/search/stream/rules', method='post', query=request_query,
                                   params=request_params, data=data, dtype='Rule', **kwargs)

    def delete_tweet_by_id(self, id, data=None, **kwargs):
        """Tweet delete by Tweet ID.

        Delete specified Tweet (in the path) by ID.

        Parameters
        ----------
        id: string
            The ID of the Tweet to be deleted.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/delete-tweets-id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/tweets/{id}', method='delete', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def find_tweet_by_id(self, id, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None,
                         user_fields=None, place_fields=None, data=None, **kwargs):
        """Tweet lookup by Tweet ID.

        Returns a variety of information about the Tweet specified by the requested ID.

        Parameters
        ----------
        id: string
            A single Tweet ID.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
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
        return self.client.request('/2/tweets/{id}', method='get', query=request_query, params=request_params,
                                   data=data, dtype='Tweet', **kwargs)

    def find_tweets_that_quote_a_tweet(self, id, max_results=None, pagination_token=None, exclude=None,
                                       tweet_fields=None, expansions=None, media_fields=None, poll_fields=None,
                                       user_fields=None, place_fields=None, data=None, **kwargs):
        """Retrieve Tweets that quote a Tweet.

        Returns a variety of information about each Tweet that quotes the Tweet specified by the requested ID.

        Parameters
        ----------
        id: string
            A single Tweet ID.
        max_results: integer, optional
            The maximum number of results to be returned.
        pagination_token: string, optional
            This parameter is used to get a specified 'page' of results.
        exclude: list[string], optional
            The set of entities to exclude (e.g. 'replies' or 'retweets').
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/quote-tweets/api-reference/get-tweets-id-quote_tweets>`__.
        
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
        if exclude is not None:
            request_query['exclude'] = exclude
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
        return self.client.request('/2/tweets/{id}/quote_tweets', method='get', query=request_query,
                                   params=request_params, data=data, dtype='Tweet', **kwargs)

    def hide_reply_by_id(self, tweet_id, data=None, **kwargs):
        """Hide replies.

        Hides or unhides a reply to an owned conversation.

        Parameters
        ----------
        tweet_id: string
            The ID of the reply that you want to hide or unhide.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/api-reference/put-tweets-id-hidden>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['tweet_id'] = tweet_id
        return self.client.request('/2/tweets/{tweet_id}/hidden', method='put', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)

    def users_id_liked_tweets(self, id, max_results=None, pagination_token=None, tweet_fields=None, expansions=None,
                              media_fields=None, poll_fields=None, user_fields=None, place_fields=None, data=None,
                              **kwargs):
        """Returns Tweet objects liked by the provided User ID.

        Returns a list of Tweets liked by the provided User ID.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-users-id-liked_tweets>`__.
        
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
        return self.client.request('/2/users/{id}/liked_tweets', method='get', query=request_query,
                                   params=request_params, data=data, dtype='Tweet', **kwargs)

    def users_id_like(self, id, data=None, **kwargs):
        """Causes the User (in the path) to like the specified Tweet.

        Causes the User (in the path) to like the specified Tweet. The User in the path must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to like the Tweet.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/post-users-id-likes>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/likes', method='post', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def users_id_unlike(self, id, tweet_id, data=None, **kwargs):
        """Causes the User (in the path) to unlike the specified Tweet.

        Causes the User (in the path) to unlike the specified Tweet. The User must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to unlike the Tweet.
        tweet_id: string
            The ID of the Tweet that the User is requesting to unlike.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/delete-users-id-likes-tweet_id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['tweet_id'] = tweet_id
        return self.client.request('/2/users/{id}/likes/{tweet_id}', method='delete', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)

    def users_id_mentions(self, id, since_id=None, until_id=None, max_results=None, pagination_token=None,
                          start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None,
                          poll_fields=None, user_fields=None, place_fields=None, data=None, **kwargs):
        """User mention timeline by User ID.

        Returns Tweet objects that mention username associated to the provided User ID.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        since_id: string, optional
            The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
        until_id: string, optional
            The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.Example: 1346889436626259968.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.Example: 2021-02-01T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.Example: 2021-02-14T18:40:40.000Z.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-mentions>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if since_id is not None:
            request_query['since_id'] = since_id
        if until_id is not None:
            request_query['until_id'] = until_id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
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
        return self.client.request('/2/users/{id}/mentions', method='get', query=request_query, params=request_params,
                                   data=data, dtype='Tweet', **kwargs)

    def users_id_retweets(self, id, data=None, **kwargs):
        """Causes the User (in the path) to retweet the specified Tweet.

        Causes the User (in the path) to retweet the specified Tweet. The User in the path must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to retweet the Tweet.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/post-users-id-retweets>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        return self.client.request('/2/users/{id}/retweets', method='post', query=request_query, params=request_params,
                                   data=data, dtype='data', **kwargs)

    def users_id_unretweets(self, id, source_tweet_id, data=None, **kwargs):
        """Causes the User (in the path) to unretweet the specified Tweet.

        Causes the User (in the path) to unretweet the specified Tweet. The User must match the User context authorizing the request.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User that is requesting to retweet the Tweet.
        source_tweet_id: string
            The ID of the Tweet that the User is requesting to unretweet.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/delete-users-id-retweets-tweet_id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        request_params['source_tweet_id'] = source_tweet_id
        return self.client.request('/2/users/{id}/retweets/{source_tweet_id}', method='delete', query=request_query,
                                   params=request_params, data=data, dtype='data', **kwargs)

    def users_id_timeline(self, id, since_id=None, until_id=None, max_results=None, pagination_token=None, exclude=None,
                          start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None,
                          poll_fields=None, user_fields=None, place_fields=None, data=None, **kwargs):
        """User home timeline by User ID.

        Returns Tweet objects that appears in the provided User ID's home timeline.

        Parameters
        ----------
        id: string
            The ID of the authenticated source User to list Reverse Chronological Timeline Tweets of.
        since_id: string, optional
            The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.Example: 791775337160081409.
        until_id: string, optional
            The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.Example: 1346889436626259968.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results.
        exclude: list[string], optional
            The set of entities to exclude (e.g. 'replies' or 'retweets').
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.Example: 2021-02-01T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.Example: 2021-02-14T18:40:40.000Z.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-reverse-chronological>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if since_id is not None:
            request_query['since_id'] = since_id
        if until_id is not None:
            request_query['until_id'] = until_id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if exclude is not None:
            request_query['exclude'] = exclude
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
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
        return self.client.request('/2/users/{id}/timelines/reverse_chronological', method='get', query=request_query,
                                   params=request_params, data=data, dtype='Tweet', **kwargs)

    def users_id_tweets(self, id, since_id=None, until_id=None, max_results=None, pagination_token=None, exclude=None,
                        start_time=None, end_time=None, tweet_fields=None, expansions=None, media_fields=None,
                        poll_fields=None, user_fields=None, place_fields=None, data=None, **kwargs):
        """User Tweets timeline by User ID.

        Returns a list of Tweets authored by the provided User ID.

        Parameters
        ----------
        id: string
            The ID of the User to lookup.Example: 2244994945.
        since_id: string, optional
            The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.Example: 791775337160081409.
        until_id: string, optional
            The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.Example: 1346889436626259968.
        max_results: integer, optional
            The maximum number of results.
        pagination_token: string, optional
            This parameter is used to get the next 'page' of results.
        exclude: list[string], optional
            The set of entities to exclude (e.g. 'replies' or 'retweets').
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.Example: 2021-02-01T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.Example: 2021-02-14T18:40:40.000Z.
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
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if since_id is not None:
            request_query['since_id'] = since_id
        if until_id is not None:
            request_query['until_id'] = until_id
        if max_results is not None:
            request_query['max_results'] = max_results
        if pagination_token is not None:
            request_query['pagination_token'] = pagination_token
        if exclude is not None:
            request_query['exclude'] = exclude
        if start_time is not None:
            request_query['start_time'] = start_time
        if end_time is not None:
            request_query['end_time'] = end_time
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
        return self.client.request('/2/users/{id}/tweets', method='get', query=request_query, params=request_params,
                                   data=data, dtype='Tweet', **kwargs)
