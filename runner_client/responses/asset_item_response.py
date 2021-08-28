from .base_response import BaseResponse
from ..models import AssetItem

class AssetItemResponse(BaseResponse):
    def _on_init(self, data):
        self.__asset_item = AssetItem(data)

    @property
    def asset_item(self):
        return self.__asset_item
