from .const import CONF_NOISE_PSK as CONF_NOISE_PSK, DOMAIN as DOMAIN
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry
from .serial_proxy import build_url as build_url
from homeassistant.components import websocket_api as websocket_api
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr
from typing import Any

TYPE: str
ENTRY_ID: str
DEVICE_ID: str
ZWAVE_JS_DOMAIN: str
_UNAVAILABLE_CAPABILITIES: dict[str, Any]

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
@websocket_api.require_admin
def get_encryption_key(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def get_device_capabilities(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _is_main_esphome_device(device: dr.DeviceEntry) -> bool: ...
def _zwave_js_config_entry_id(hass: HomeAssistant, home_id: int) -> str | None: ...
