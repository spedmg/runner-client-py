from .. import http
from ..responses import AssetItemResponse

def get_asset_item(asset_id):
    response = http.get(f'asset_items/{asset_id}')
    return AssetItemResponse(response)
