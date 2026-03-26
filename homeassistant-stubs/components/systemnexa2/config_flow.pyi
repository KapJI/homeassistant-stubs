from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE, SOURCE_USER as SOURCE_USER
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.util.network import is_ip_address as is_ip_address
from typing import Any

_LOGGER: Incomplete
_SCHEMA: Incomplete

@dataclass(kw_only=True)
class _DiscoveryInfo:
    name: str
    host: str
    model: str
    device_id: str
    device_version: str

class SystemNexa2ConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_device: _DiscoveryInfo
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _async_set_unique_id(self) -> None: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_create_device_entry(self) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_is_valid_host(self, ip_or_hostname: str) -> bool: ...
