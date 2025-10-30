from .const import CONF_GROUP as CONF_GROUP, DOMAIN as DOMAIN, GROUPS as GROUPS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from typing import Any

_LOGGER: Incomplete

async def validate_input(hass: HomeAssistant, user_input: dict[str, Any], data: dict[str, Any] | None = None) -> dict[str, Any]: ...

class SmaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _data: dict[str, Any]
    _discovery_data: dict[str, Any]
    def __init__(self) -> None: ...
    async def _handle_user_input(self, user_input: dict[str, Any], discovery: bool = False) -> tuple[dict[str, str], dict[str, str]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
