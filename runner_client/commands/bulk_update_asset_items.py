from .. import http
from ..responses import BulkUpdateResponse

def bulk_update_asset_items(asset_items):
    raw_response = http.post('asset_items/bulk_update', { 'asset_items': asset_items })
    return BulkUpdateResponse(raw_response)
