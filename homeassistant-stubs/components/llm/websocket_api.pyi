from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.llm import async_get_apis as async_get_apis
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@callback
def websocket_list_apis(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
