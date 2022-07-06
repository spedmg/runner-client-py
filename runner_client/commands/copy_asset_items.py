from .. import http
from ..responses import BaseResponse
from ..exceptions import InvalidParameterException

def copy_asset_items(
    asset_item_ids,
    destination_folder_ids,
    source_folder_id=None,
    remove_from_source=False
):
    if remove_from_source and not source_folder_id:
        raise InvalidParameterException(
            'source_folder_id is required when remove_from_source is True'
        )
    if not destination_folder_ids:
        raise InvalidParameterException('destination_folder_ids is required')

    body = {
        'asset_item_ids': asset_item_ids,
        'destination_folder_ids': destination_folder_ids
    }
    if remove_from_source:
        body['remove_from_source'] = True
        body['source_folder_id'] = source_folder_id

    raw_response = http.post('asset_items/copy', body)
    return BaseResponse(raw_response)
