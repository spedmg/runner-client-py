from .. import http
from ..responses import BaseResponse
from ..exceptions import InvalidParameterException

REQUIRED = (
        'destination_file_path',
        'credentials',
        'asset_items'
        )

def create_push_transfer(protocol='s3', **opts):
    body = dict(transfer_type='push delivery', protocol=protocol, **opts)
    for prop in REQUIRED:
        if not body.get(prop):
            raise InvalidParameterException(f'{prop} is required')

    response = http.post('transfers', body)
    return BaseResponse(response)
