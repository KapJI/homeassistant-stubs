from .const import DATA_MANAGER as DATA_MANAGER
from .manager import ManagerStateEvent as ManagerStateEvent
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.backup import async_subscribe_events as async_subscribe_events
from typing import Any

@callback
def async_register_websocket_handlers(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_subscribe_events(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
