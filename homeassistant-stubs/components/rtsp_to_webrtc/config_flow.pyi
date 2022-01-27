from . import DATA_SERVER_URL as DATA_SERVER_URL, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Any
DATA_SCHEMA: Any

class RTSPToWebRTCConfigFlow(config_entries.ConfigFlow):
    _hassio_discovery: dict[str, Any]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _test_connection(self, url: str) -> Union[str, None]: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
    async def async_step_hassio_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
