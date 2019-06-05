import certifi
import urllib3

import teapot


class HTTPClient:
    def __init__(self, base_url="", headers=None, **kwargs):
        # TODO: do something with the kwargs and de-hard code the cert stuff
        self.base_url = base_url
        self._http = urllib3.PoolManager(
            cert_reqs="CERT_REQUIRED",
            ca_certs=certifi.where(),
            headers=headers)

    def _get_uri(self, url):
        if self.base_url != "":
            return self.base_url + url
        return url

    def _request(self, method, uri, **kwargs):
        r = self._http.request(method, uri, **kwargs)
        resp = teapot.HTTPResponse(r)
        if 400 <= resp.status:
            raise resp.raise_for_status()
        return resp

    def request(self, method, url, **kwargs):
        return self._request(method.upper(), self._get_uri(url), **kwargs)

    def head(self, url, **kwargs):
        return self.request("HEAD", url, **kwargs)

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self.request("PUT", url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)

    def patch(self, url, **kwargs):
        return self.request("PATCH", url, **kwargs)

    def options(self, url, **kwargs):
        return self.request("OPTIONS", url, **kwargs)
