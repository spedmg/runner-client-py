from .. import http
from ..responses import BaseResponse
from ..exceptions import InvalidParameterException

def restore_assets(**body):
    if not body.get('asset_item_ids'):
        raise InvalidParameterException('asset_item_ids is required')

    response = http.post('asset_items/restores', body)
    return BaseResponse(response)
