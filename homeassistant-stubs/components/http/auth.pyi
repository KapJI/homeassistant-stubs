from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID, KEY_HASS_USER as KEY_HASS_USER
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Any
DATA_API_PASSWORD: str
DATA_SIGN_SECRET: str
SIGN_QUERY_PARAM: str

def async_sign_path(hass: Any, refresh_token_id: Any, path: Any, expiration: Any): ...
def setup_auth(hass: Any, app: Any): ...
