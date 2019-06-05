import certifi
import urllib3

import teapot


class HTTPClient:
    def __init__(self, base_url="", **kwargs):
        self.base_url = base_url

        if not kwargs:
            kwargs = {}
        if "cert_reqs" not in kwargs:
            kwargs["cert_reqs"] = "CERT_REQUIRED"
        if "ca_certs" not in kwargs:
            kwargs["ca_certs"] = certifi.where()

        self._http = urllib3.PoolManager(**kwargs)

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
