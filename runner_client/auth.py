# pylint: disable=no-member
from datetime import datetime
import requests
from . import config

class AuthData(dict):
    __FIELDS = ('access_token', 'refresh_token', 'created_at', 'expires_in')

    def __init__(self, auth_data=None):
        auth_data = auth_data or {}
        for field in AuthData.__FIELDS:
            setattr(self, field, auth_data.get(field))
        dict.__init__(self, **auth_data)

    @property
    def token_expiry(self):
        return (self.created_at or 0) + (self.expires_in or 0)

    def token_expired(self):
        expiry = self.token_expiry
        if expiry:
            now = int(datetime.now().timestamp())
            return (now + 5) > expiry
        return True

    def update(self, auth_data):
        for field in AuthData.__FIELDS:
            setattr(self, field, auth_data.get(field))
        super().update(auth_data)
        return self

    def fetch_new_token(self):
        if self.refresh_token:
            # refresh API token
            self.__auth_request({
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
                })
        else:
            # New API Session
            self.__auth_request({
                'grant_type': 'password',
                'username': config.username,
                'password': config.password,
                })

    def authorization_grant(self, code, redirect_uri):
        '''
        For authorization-grant oauth flows
        {"client_id": "XXXX", "client_secret": "XXX", "redirect_uri": "https://your.redirect.uri",
         "code": "code_from_step_1", "grant_type": "authorization_code"}
        '''
        return self.__auth_request({
            'redirect_uri':  redirect_uri,
            'code':          code,
            'grant_type':    'authorization_code'
            })

    def __auth_request(self, body):
        url = f'{config.base_url}/oauth/token'
        auth = None
        if config.client_id and config.client_secret:
            auth = (config.client_id, config.client_secret)
        elif config.username and config.password:
            auth = (config.username, config.password)

        response = requests.post(url, data=body, auth=auth)

        if response.ok:
            response_data = response.json()
            return self.update(response_data)

        raise Exception(f'Runner authentication failed: {response.text}')

    def reset(self):
        for field in AuthData.__FIELDS:
            setattr(self, field, None)

current_auth_data = AuthData()

def access_token():
    if current_auth_data.token_expired():
        current_auth_data.fetch_new_token()
    return current_auth_data.access_token

def authorization_grant(*args, **kwargs):
    return current_auth_data.authorization_grant(*args, **kwargs)

def set_auth_tokens(response_data):
    current_auth_data.update(response_data)
    return current_auth_data

def reset():
    current_auth_data.reset()
    return current_auth_data
