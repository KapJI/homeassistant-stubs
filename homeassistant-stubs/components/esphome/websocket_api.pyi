from .const import CONF_NOISE_PSK as CONF_NOISE_PSK
from _typeshed import Incomplete
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

_LOGGER: Incomplete
TYPE: str
ENTRY_ID: str

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
@websocket_api.require_admin
def get_encryption_key(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
