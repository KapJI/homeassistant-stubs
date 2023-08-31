from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

class NamConfig:
    mac_address: str
    auth_enabled: bool
    def __init__(self, mac_address, auth_enabled) -> None: ...

_LOGGER: Incomplete
AUTH_SCHEMA: Incomplete

async def async_get_config(hass: HomeAssistant, host: str) -> NamConfig: ...
async def async_check_credentials(hass: HomeAssistant, host: str, data: dict[str, Any]) -> None: ...

class NAMFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: Incomplete
    entry: Incomplete
    _config: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_credentials(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
