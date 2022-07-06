from .base_response import BaseResponse
from ..models import AssetItem

class BulkUpdateResponse(BaseResponse):
    def _on_init(self, data):
        self.__asset_items = [AssetItem(**item) for item in data['bulk_update']]

    @property
    def asset_items(self):
        return self.__asset_items
