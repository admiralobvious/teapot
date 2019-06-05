import logging

USING_RAPIDJSON = False
try:
    import rapidjson as json
    USING_RAPIDJSON = True
except ImportError:  # pragma: no cover
    import json  # pragma: no cover

json = json

from .api import HTTPAPI
from .client import HTTPClient
from .exceptions import HTTPResponseError
from .response import HTTPResponse

log = logging.getLogger("teapot")
