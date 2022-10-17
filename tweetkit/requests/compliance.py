"""All methods related to compliance."""
from tweetkit.models import Paginator, TwitterStreamResponse, TwitterResponse

__all__ = [
    'Compliance'
]


class Compliance(object):
    """Endpoints related to keeping Twitter data in your systems compliant"""

    def __init__(self, client):
        self.client = client

    def list_batch_compliance_jobs(self, type, status=None, compliance_job_fields=None, data=None, **kwargs):
        """List Compliance Jobs.

        Returns recent Compliance Jobs for a given job type and optional job status.

        Parameters
        ----------
        type: string
            Type of Compliance Job to list.
        status: string, optional
            Status of Compliance Job to list.
        compliance_job_fields: list[string], optional
            A comma separated list of ComplianceJob fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_query['type'] = type
        if status is not None:
            request_query['status'] = status
        if compliance_job_fields is not None:
            request_query['compliance_job.fields'] = compliance_job_fields
        else:
            request_query['compliance_job.fields'] = ['created_at', 'download_expires_at', 'download_url', 'id', 'name',
                                                      'resumable', 'status', 'type', 'upload_expires_at', 'upload_url']
        return self.client.request('/2/compliance/jobs', method='get', query=request_query, params=request_params,
                                   data=data, dtype='ComplianceJob', **kwargs)

    def create_batch_compliance_job(self, data, **kwargs):
        """Create compliance job.

        Creates a compliance for the given job type.

        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/post-compliance-jobs>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        return self.client.request('/2/compliance/jobs', method='post', query=request_query, params=request_params,
                                   data=data, dtype='ComplianceJob', **kwargs)

    def get_batch_compliance_job(self, id, compliance_job_fields=None, data=None, **kwargs):
        """Get Compliance Job.

        Returns a single Compliance Job by ID.

        Parameters
        ----------
        id: string
            The ID of the Compliance Job to retrieve.
        compliance_job_fields: list[string], optional
            A comma separated list of ComplianceJob fields to display.
        data: dict
            The request body.
        
        Notes
        -----
        For more information, see: `here <https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id>`__.
        
        Returns
        -------
        session: TwitterStreamResponse or TwitterResponse or Paginator
            A object with the response data.
        """
        request_params, request_query = {}, {}
        request_params['id'] = id
        if compliance_job_fields is not None:
            request_query['compliance_job.fields'] = compliance_job_fields
        else:
            request_query['compliance_job.fields'] = ['created_at', 'download_expires_at', 'download_url', 'id', 'name',
                                                      'resumable', 'status', 'type', 'upload_expires_at', 'upload_url']
        return self.client.request('/2/compliance/jobs/{id}', method='get', query=request_query, params=request_params,
                                   data=data, dtype='ComplianceJob', **kwargs)

    def get_tweets_compliance_stream(self, partition, backfill_minutes=None, start_time=None, end_time=None, data=None,
                                     **kwargs):
        """Tweets Compliance stream.

        Streams 100% of compliance data for Tweets.

        Parameters
        ----------
        partition: integer
            The partition number.
        backfill_minutes: integer, optional
            The number of minutes of backfill requested.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet Compliance events will be provided.Example: 2021-02-01T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweet Compliance events will be provided.Example: 2021-02-14T18:40:40.000Z.
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
        return self.client.request('/2/tweets/compliance/stream', method='get', query=request_query,
                                   params=request_params, data=data, stream=True, **kwargs)

    def get_users_compliance_stream(self, partition, backfill_minutes=None, start_time=None, end_time=None, data=None,
                                    **kwargs):
        """Users Compliance stream.

        Streams 100% of compliance data for Users.

        Parameters
        ----------
        partition: integer
            The partition number.
        backfill_minutes: integer, optional
            The number of minutes of backfill requested.
        start_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.Example: 2021-02-01T18:40:40.000Z.
        end_time: string, optional
            YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.Example: 2021-02-01T18:40:40.000Z.
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
        return self.client.request('/2/users/compliance/stream', method='get', query=request_query,
                                   params=request_params, data=data, stream=True, **kwargs)
