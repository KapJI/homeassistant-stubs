from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from pooldose.type_definitions import APIVersionResponse as APIVersionResponse
from typing import Any

_LOGGER: Incomplete
SCHEMA_DEVICE: Incomplete

class PooldoseConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _discovered_ip: str | None
    _discovered_mac: str | None
    def __init__(self) -> None: ...
    async def _validate_host(self, host: str) -> tuple[str | None, APIVersionResponse | None, dict[str, str] | None]: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_dhcp_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
