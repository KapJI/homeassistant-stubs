from .const import DATA_COMPONENT as DATA_COMPONENT, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import ERR_NOT_FOUND as ERR_NOT_FOUND, ERR_NOT_SUPPORTED as ERR_NOT_SUPPORTED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_register_websocket_handlers(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def handle_get_segments(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
