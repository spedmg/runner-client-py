import requests

from . import config
from . import auth

def get(uri, params=None, version='v1'):
    url = __url(uri, version)
    if not params:
        params = {}
    return requests.get(
            url,
            params=params,
            headers=__auth_headers()
            )

def post(uri, data, version='v1'):
    url = __url(uri, version)
    if not data:
        data = {}
    return requests.post(
            url,
            json=data,
            headers=__auth_headers()
            )

def __url(uri, version='v1'):
    return str.join('/', [
        config.base_url,
        'api',
        version,
        uri
        ])

def __auth_headers():
    token = auth.access_token()
    return { 'Authorization': f'Bearer {token}' }
