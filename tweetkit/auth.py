"""TwitterAuth"""
from __future__ import absolute_import

import inspect

from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import AuthBase
from requests.exceptions import RequestException
from requests_oauthlib import OAuth1Session, OAuth2Session, OAuth1


class TokenAuth(AuthBase):
    """Token"""

    # noinspection PyShadowingBuiltins
    def __init__(self, type, scheme):
        super(TokenAuth, self).__init__()
        self.type = type
        self.scheme = scheme

    def __iter__(self):
        for param in inspect.signature(type(self)).parameters.keys():
            yield getattr(self, param)

    def refresh(self):
        """refresh"""
        return self

    def __call__(self, r):
        """Add auth parameters to the request."""
        self.refresh()
        return r


class BearerTokenAuth(TokenAuth):
    """BearerToken"""

    def __init__(self, bearer_token=None):
        super(BearerTokenAuth, self).__init__(type='http', scheme='bearer')
        self.bearer_token = bearer_token

    def __call__(self, r):
        """Add OAuth parameters to the request."""
        r = super(BearerTokenAuth, self).__call__(r)
        r.headers['Authorization'] = 'Bearer {}'.format(self.bearer_token)
        return r


class OAuth2UserTokenAuth(TokenAuth):
    """OAuth2UserToken"""

    def __init__(self, consumer_key, consumer_secret, bearer_token=None, client_credentials=True):
        super(OAuth2UserTokenAuth, self).__init__(type='oauth2', scheme=None)
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.bearer_token = bearer_token
        self.client_credentials = client_credentials

    def refresh(self):
        """refresh"""
        if not self.bearer_token:
            client = BackendApplicationClient(client_id=self.consumer_key)
            oauth = OAuth2Session(client=client)
            token_url = 'https://api.twitter.com/oauth2/token'
            if self.client_credentials:
                token_url += '?grant_type=client_credentials'
            self.bearer_token = oauth.fetch_token(
                token_url=token_url, client_id=self.consumer_key,
                client_secret=self.consumer_secret
            )
        return self

    def __call__(self, r):
        """Add OAuth parameters to the request."""
        r = super(OAuth2UserTokenAuth, self).__call__(r)
        r.headers['Authorization'] = 'Bearer {}'.format(self.bearer_token)
        return r


class UserTokenAuth(TokenAuth):
    """UserToken"""

    def __init__(self, consumer_key, consumer_secret, access_token=None, token_secret=None):
        super(UserTokenAuth, self).__init__(type='http', scheme='OAuth')
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = token_secret
        self.user_id = None
        self.screen_name = None

    def refresh(self):
        """Refresh token.

        Updates access token of the user if not provided.

        Returns
        -------
        None
        """
        if self.access_token is None or self.access_token_secret is None:
            oauth_token, oauth_token_secret = self.request_token()
            authorization_pin = self.get_user_authorization(oauth_token)
            access_token, access_token_secret, user_id, screen_name = self.get_user_access_tokens(
                oauth_token,
                oauth_token_secret,
                authorization_pin
            )
            self.access_token = access_token
            self.access_token_secret = access_token_secret
            self.user_id = user_id
            self.screen_name = screen_name
        return self

    def request_token(self):
        """Request token.

        Returns
        -------
        oauth_token: str
            Token.
        oauth_token_secret: str
            Secret.
        """
        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret, callback_uri='oob')
        url = "https://api.twitter.com/oauth/request_token"
        try:
            response = oauth.fetch_request_token(url)
            oauth_token = response.get('oauth_token')
            oauth_token_secret = response.get('oauth_token_secret')
        except RequestException as ex:
            raise ex
        else:
            return oauth_token, oauth_token_secret

    # noinspection PyMethodMayBeStatic
    def get_user_authorization(self, oauth_token):
        """Generate a set of user Access Tokens.

        This is the second step in the OAuth 1.0a 3-legged OAuth flow,
        which can be used to generate a set of user Access Tokens.

        Parameters
        ----------
        oauth_token: str
            Pass the value of the oauth_token received via the POST oauth/request_token
            endpoint as the value of this parameter.
        Returns
        -------
        authorization_pin: str
            The authorization pin obtained through Twitter.
        """
        authorization_url = 'https://api.twitter.com/oauth/authorize?oauth_token={}'.format(oauth_token)
        authorization_pin = input(
            'Send the following URL to the user you want to generate access tokens for. \n'
            '→ {authorization_url} \n'
            'This URL will allow the user to authorize your application and generate a PIN. \n '
            'Paste PIN here: '.format(authorization_url=authorization_url))
        return authorization_pin

    def get_user_access_tokens(self, oauth_token, oauth_token_secret, authorization_pin):
        """Exchange the OAuth Request Token for the user’s Access Tokens.

        Parameters
        ----------
        oauth_token: str
            The OAuth token.
        oauth_token_secret
            The OAuth token secret.
        authorization_pin
            The authorization pin.

        Returns
        -------
        access_token: str
            The access token.
        access_token_secret: str
            The access token secret.
        user_id: str
            The user ID.
        screen_name: str
            The screen name of user.
        """
        oauth = OAuth1Session(
            client_key=self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_token_secret,
            verifier=authorization_pin
        )
        url = 'https://api.twitter.com/oauth/access_token'
        try:
            response = oauth.fetch_access_token(url)
        except RequestException as ex:
            raise ex
        else:
            access_token = response['oauth_token']
            access_token_secret = response['oauth_token_secret']
            user_id = response['user_id']
            screen_name = response['screen_name']
            return access_token, access_token_secret, user_id, screen_name

    def __call__(self, r):
        """Add OAuth parameters to the request."""
        r = super(UserTokenAuth, self).__call__(r)
        return OAuth1(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret
        )(r)
