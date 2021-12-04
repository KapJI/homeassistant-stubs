from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID, KEY_HASS_USER as KEY_HASS_USER
from .request_context import current_request as current_request
from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from datetime import timedelta
from homeassistant.auth.models import User as User
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.network import is_local as is_local
from typing import Any, Final

_LOGGER: Any
DATA_API_PASSWORD: Final[str]
DATA_SIGN_SECRET: Final[str]
SIGN_QUERY_PARAM: Final[str]

def async_sign_path(hass: HomeAssistant, refresh_token_id: str, path: str, expiration: timedelta) -> str: ...
def async_user_not_allowed_do_auth(hass: HomeAssistant, user: User, request: Union[Request, None] = ...) -> Union[str, None]: ...
def setup_auth(hass: HomeAssistant, app: Application) -> None: ...
