from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID, KEY_HASS_USER as KEY_HASS_USER
from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Final

_LOGGER: Any
DATA_API_PASSWORD: Final[str]
DATA_SIGN_SECRET: Final[str]
SIGN_QUERY_PARAM: Final[str]

def async_sign_path(hass: HomeAssistant, refresh_token_id: str, path: str, expiration: timedelta) -> str: ...
def setup_auth(hass: HomeAssistant, app: Application) -> None: ...
