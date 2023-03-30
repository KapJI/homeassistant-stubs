from .const import VALID_UNITS as VALID_UNITS
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

def async_setup(hass: HomeAssistant) -> None: ...
def ws_convertible_units(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
