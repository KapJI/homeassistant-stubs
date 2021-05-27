from aiohttp.web import Application as Application
from aiohttp.web_urldispatcher import AbstractResource as AbstractResource
from homeassistant.const import HTTP_HEADER_X_REQUESTED_WITH as HTTP_HEADER_X_REQUESTED_WITH
from homeassistant.core import callback as callback
from typing import Any, Final

ALLOWED_CORS_HEADERS: Final[list[str]]
VALID_CORS_TYPES: Final[Any]

def setup_cors(app: Application, origins: list[str]) -> None: ...
