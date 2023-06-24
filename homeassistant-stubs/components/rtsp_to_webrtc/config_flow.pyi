from . import CONF_STUN_SERVER as CONF_STUN_SERVER, DATA_SERVER_URL as DATA_SERVER_URL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete
DATA_SCHEMA: Incomplete

class RTSPToWebRTCConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    _hassio_discovery: dict[str, Any]
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _test_connection(self, url: str) -> str | None: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
    async def async_step_hassio_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
