from . import KaleidescapeDeviceInfo as KaleidescapeDeviceInfo, UnsupportedError as UnsupportedError, validate_host as validate_host
from .const import DEFAULT_HOST as DEFAULT_HOST, DOMAIN as DOMAIN
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigFlow as ConfigFlow
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

ERROR_CANNOT_CONNECT: str
ERROR_UNSUPPORTED: str

class KaleidescapeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_device: KaleidescapeDeviceInfo
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict | None = ...) -> FlowResult: ...
