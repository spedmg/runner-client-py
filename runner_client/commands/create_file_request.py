from .. import http
from ..responses import FileRequestResponse
from ..exceptions import InvalidParameterException

def create_file_request(**body):
    if 'folder_id' not in body:
        raise InvalidParameterException('folder_id is required')
    if 'expiration' not in body:
        raise InvalidParameterException('expiration is required')

    response = http.post('file_requests', body)
    return FileRequestResponse(response)
