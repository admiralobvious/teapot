from urllib3.exceptions import HTTPError


class HTTPResponseError(HTTPError):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return "{} {} for url {}".format(self.response.status, self.response.reason, self.response.geturl())
