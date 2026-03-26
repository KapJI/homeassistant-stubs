from aiohttp.web import Request as Request
from homeassistant.helpers.http import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS
from typing import Final

DOMAIN: Final[str]
KEY_HASS_USER: Final[str]
KEY_HASS_REFRESH_TOKEN_ID: Final[str]

def is_supervisor_unix_socket_request(request: Request) -> bool: ...
