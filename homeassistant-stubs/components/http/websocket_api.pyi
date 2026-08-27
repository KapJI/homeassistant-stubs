from .config import ConfData as ConfData, HTTP_STORAGE_SCHEMA as HTTP_STORAGE_SCHEMA, async_get_and_load_store as async_get_and_load_store
from .const import ATTR_CONFIG as ATTR_CONFIG, CONF_SERVER_PORT as CONF_SERVER_PORT, CONF_TRUSTED_PROXIES as CONF_TRUSTED_PROXIES, CONF_USE_X_FORWARDED_FOR as CONF_USE_X_FORWARDED_FOR
from .server import async_verify_can_bind as async_verify_can_bind
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.homeassistant import SERVICE_HOMEASSISTANT_RESTART as SERVICE_HOMEASSISTANT_RESTART
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Final

ERR_BIND_FAILED: Final[str]
ERR_NOT_RUNNING: Final[str]

def _validate_trusted_proxies(config: ConfData) -> ConfData: ...
@callback
def async_register_websocket_commands(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_get_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_set_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_promote_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
