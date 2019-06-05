import urllib3

from . import json
from .exceptions import HTTPResponseError


class HTTPResponse(urllib3.HTTPResponse):
    def __init__(self, response):
        for k, v in response.__dict__.items():
            self.__dict__[k] = v

    def json(self, ):
        return json.loads(self.data.decode("utf-8"))

    def raise_for_status(self):
        raise HTTPResponseError(self)

    def __str__(self):
        return f"<{self.__class__.__name__} [{self.status}]>"
