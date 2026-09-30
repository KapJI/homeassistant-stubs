from .connection import async_get_connection_info as async_get_connection_info
from .const import DATA_MODBUS_HUBS as DATA_MODBUS_HUBS
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Final

TYPE_LIST_CONNECTIONS: Final[str]
SOURCE_CONFIG_ENTRY: Final[str]
SOURCE_YAML: Final[str]

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@callback
def websocket_list_connections(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
