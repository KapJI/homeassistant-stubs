from .const import DOMAIN as DOMAIN, SSDP_SCANNER as SSDP_SCANNER
from .scanner import Scanner as Scanner, SsdpChange as SsdpChange
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.json import json_bytes as json_bytes
from homeassistant.helpers.service_info.ssdp import ATTR_UPNP_FRIENDLY_NAME as ATTR_UPNP_FRIENDLY_NAME, SsdpServiceInfo as SsdpServiceInfo
from typing import Any, Final

FIELD_SSDP_ST: Final[str]
FIELD_SSDP_LOCATION: Final[str]

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def ws_subscribe_discovery(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
