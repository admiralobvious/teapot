import json

import teapot
from teapot import USING_RAPIDJSON

from . import TestBase, responses


class TestClient(TestBase):
    def setUp(self):
        self.base_setup()

    def test_base_uri(self):
        base_url = "http://localhost"
        c = teapot.HTTPClient(base_url=base_url)
        endpoint = "/foo/bar"
        assert c._get_uri(endpoint) == base_url+endpoint

    @responses.activate
    def test_response(self):
        responses.add("GET", "/foo/bar",
                      body="text", status=200,
                      content_type="text/plain")

        resp = self.client.get("http://localhost/foo/bar")

        assert resp.data == b"text"
        assert resp.status == 200
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == "/foo/bar"
        assert responses.calls[0].request.host == "localhost"
        assert responses.calls[0].request.scheme == "http"

    @responses.activate
    def test_json_response(self):
        responses.add("GET", "/hello",
                      body="{\"hello\": \"world\"}", status=200,
                      content_type="application/json")

        resp = self.client.get("http://localhost/hello")

        assert resp.json() == {"hello": "world"}

    @responses.activate
    def test_invalid_json_response(self):
        responses.add("GET", "/",
                      body="not json", status=200,
                      content_type="text/plain")

        resp = self.client.get("http://localhost/")

        if USING_RAPIDJSON:
            self.assertRaises(ValueError, resp.json)
        else:
            self.assertRaises(json.decoder.JSONDecodeError, resp.json)

    @responses.activate
    def test_4xx_raises_response_error(self):
        responses.add("GET", "/",
                      body="text", status=400,
                      content_type="text/plain")

        self.assertRaises(teapot.exceptions.HTTPResponseError,
                          self.client.get, "http://localhost/")
