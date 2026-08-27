from .const import CONF_MODBUS_PORT as CONF_MODBUS_PORT, DEFAULT_MODBUS_PORT as DEFAULT_MODBUS_PORT, DOMAIN as DOMAIN, FroniusConfigEntryData as FroniusConfigEntryData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from typing import Any, Final, override

_LOGGER: Final[Incomplete]
DHCP_REQUEST_DELAY: Final[int]
MODBUS_PORT_SELECTOR: Final[Incomplete]

def create_title(info: FroniusConfigEntryData) -> str: ...
async def validate_host(hass: HomeAssistant, host: str, modbus_port: int = ...) -> tuple[str, FroniusConfigEntryData]: ...

class FroniusConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    info: FroniusConfigEntryData
    def __init__(self) -> None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
