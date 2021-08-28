class BaseResponse:
    def __init__(self, response):
        self.__response = response
        if response.ok:
            self._on_init(response.json())

    @property
    def ok(self):
        return self.__response.ok

    def json(self):
        return self.__response.json()

    def _on_init(self, data):
        pass
