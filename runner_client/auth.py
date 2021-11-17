from datetime import datetime
import requests
from . import config

__AUTHDATA = {
        '__current_token': None,
        '__current_refresh_token': None,
        '__token_expiry': 0,
        }

def access_token():
    if token_expired():
        __fetch_new_token()
    return __AUTHDATA['__current_token']

def token_expired():
    expiry = __AUTHDATA['__token_expiry']
    if expiry:
        now = int(datetime.now().timestamp())
        return (now + 5) > expiry
    return True

def authorization_grant(code, redirect_uri, client_id=None, client_secret=None):
    '''
    For authorization-grant oauth flows
    {"client_id": "XXXX",
     "client_secret": "XXX",
     "redirect_uri": "https://your.redirect.uri",
     "code": "code_from_step_1",
     "grant_type": "authorization_code"}
    '''
    return __auth_request({
        'client_id':     client_id or config.client_id,
        'client_secret': client_secret or config.client_secret,
        'redirect_uri':  redirect_uri,
        'code':          code,
        'grant_type':    'authorization_code'
        })

def __fetch_new_token():
    if __AUTHDATA['__current_refresh_token']:
        # refresh API token
        __auth_request({
            'grant_type': 'refresh_token',
            'refresh_token': __AUTHDATA['__current_refresh_token'],
            })
    else:
        # New API Session
        __auth_request({
            'grant_type': 'password',
            'username': config.username,
            'password': config.password,
            })

def __auth_request(body):
    url = f'{config.base_url}/oauth/token'
    response = requests.post(url, json=body)

    if response.ok:
        response_data = response.json()
        __AUTHDATA['__current_token'] = response_data['access_token']
        __AUTHDATA['__current_refresh_token'] = response_data['refresh_token']
        __AUTHDATA['__token_expiry'] = response_data['created_at'] + response_data['expires_in']
        return response_data

    raise Exception(f'Runner authentication failed: {response.text}')
