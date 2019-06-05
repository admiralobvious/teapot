import unittest

from teapot import HTTPAPI, HTTPClient
from urllib3_mock import Responses

responses = Responses("urllib3")


class TestBase(unittest.TestCase):
    def base_setup(self):
        self.client = HTTPClient()
        self.api = HTTPAPI(custom_attr="foobar")
        self.api.client = self.client
