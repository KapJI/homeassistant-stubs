from .const import CONF_URL_PATH as CONF_URL_PATH, ConfigNotFound as ConfigNotFound, LOVELACE_DATA as LOVELACE_DATA
from .dashboard import LovelaceConfig as LovelaceConfig
from .resources import ResourceStorageCollection as ResourceStorageCollection
from collections.abc import Awaitable, Callable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.json import json_fragment as json_fragment
from typing import Any

type AsyncLovelaceWebSocketCommandHandler[_R] = Callable[[HomeAssistant, websocket_api.ActiveConnection, dict[str, Any], LovelaceConfig], Awaitable[_R]]
def _handle_errors[_R](func: AsyncLovelaceWebSocketCommandHandler[_R]) -> websocket_api.AsyncWebSocketCommandHandler: ...
@websocket_api.async_response
async def websocket_lovelace_resources(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_lovelace_resources_impl(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
@_handle_errors
async def websocket_lovelace_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], config: LovelaceConfig) -> json_fragment: ...
@websocket_api.require_admin
@websocket_api.async_response
@_handle_errors
async def websocket_lovelace_save_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], config: LovelaceConfig) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
@_handle_errors
async def websocket_lovelace_delete_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any], config: LovelaceConfig) -> None: ...
