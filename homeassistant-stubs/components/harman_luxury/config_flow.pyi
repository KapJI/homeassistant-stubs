from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioharmanluxury import DeviceInfo as DeviceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.ssdp import ATTR_UPNP_SERIAL as ATTR_UPNP_SERIAL, SsdpServiceInfo as SsdpServiceInfo
from typing import Any, override

STEP_USER_DATA_SCHEMA: Incomplete

class HarmanLuxuryConfigFlow(ConfigFlow, domain=DOMAIN):
    _host: str
    _name: str
    async def _async_get_info(self, host: str) -> DeviceInfo | None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
