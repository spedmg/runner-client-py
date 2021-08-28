from .base_response import BaseResponse
from ..models import FileRequest

class FileRequestResponse(BaseResponse):
    def _on_init(self, data):
        self.__file_request = FileRequest(data)

    @property
    def file_request(self):
        return self.__file_request
