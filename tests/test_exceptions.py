import urllib3
from teapot import HTTPResponseError

from . import TestBase


class TestExceptions(TestBase):
    def setUp(self):
        self.base_setup()

    def test_http_response_error(self):
        r = urllib3.HTTPResponse(status=400, reason="Bad Request", request_url="http://localhost")
        ex = HTTPResponseError(r)
        assert str(ex) == "400 Bad Request for url http://localhost"
