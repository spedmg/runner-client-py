from .. import http
from ..responses import AssetItemResponse

def get_asset_item(id):
    response = http.get(f'asset_items/{id}')
    return AssetItemResponse(response)
