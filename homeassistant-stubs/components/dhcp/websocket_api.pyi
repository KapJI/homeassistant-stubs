from .const import HOSTNAME as HOSTNAME, IP_ADDRESS as IP_ADDRESS
from .helpers import async_get_address_data_internal as async_get_address_data_internal, async_register_dhcp_callback_internal as async_register_dhcp_callback_internal
from .models import DHCPAddressData as DHCPAddressData
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.json import json_bytes as json_bytes
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def ws_subscribe_discovery(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
