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

def __fetch_new_token():
    response = None
    url = f'{config.base_url}/oauth/token'
    if __AUTHDATA['__current_refresh_token']:
        # refresh API token
        response = requests.post(url, json={
            'grant_type': 'refresh_token',
            'refresh_token': __AUTHDATA['__current_refresh_token'],
            })
    else:
        # New API Session
        response = requests.post(url, json={
            'grant_type': 'password',
            'username': config.username,
            'password': config.password,
            })
    if response.ok:
        response_data = response.json()
        __AUTHDATA['__current_token'] = response_data['access_token']
        __AUTHDATA['__current_refresh_token'] = response_data['refresh_token']
        __AUTHDATA['__token_expiry'] = response_data['created_at'] + response_data['expires_in']
