"""All methods related to general."""

__all__ = [
    'General'
]


class General(object):
    """Miscellaneous endpoints for general API functionality"""
    
    def __init__(self, client):
        self.client = client

    def get_open_api_spec(self, data=None):
        """Returns the OpenAPI Specification document.

        Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md).

        Notes
        -----
        For more information, see: `here <None>`__.
        
        Returns
        -------
        obj: TwitterObject
            A object with the response data.
        """
        request_params, request_query = {}, {}
        return self.client.request('/2/openapi.json', method='get', query=request_query, params=request_params, data=data)
        
