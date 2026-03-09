from .const import LABS_DATA as LABS_DATA
from .helpers import async_is_preview_feature_enabled as async_is_preview_feature_enabled, async_subscribe_preview_feature as async_subscribe_preview_feature, async_update_preview_feature as async_update_preview_feature
from .models import EventLabsUpdatedData as EventLabsUpdatedData
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.backup import async_get_manager as async_get_manager
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
@websocket_api.require_admin
def websocket_list_preview_features(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_update_preview_feature(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_subscribe_feature(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
