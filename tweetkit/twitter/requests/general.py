"""All methods related to general."""
from tweetkit.twitter.exceptions import TwitterException
from tweetkit.twitter.response import Response

__all__ = [
    'General'
]


class General(object):
    """Miscellaneous endpoints for general API functionality"""

    def __init__(self, client):
        self.client = client

    def get_open_api_spec(self):
        """Returns the OpenAPI Specification document.

        Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md).

        

        Notes
        -----
        For more information, see: `here <None>`__.
        
        Returns
        -------
        response: Response
            The response object of the request.
        """
        params, query = {}, {}
        r = self.client.request('/2/openapi.json', method='get', query=query, params=params)
        content_type = r.headers.get('content-type')
        if r.status_code == 200:
            if content_type == 'application/json':
                return Response(data=r.json(), message='The request was successful')
        raise TwitterException()
