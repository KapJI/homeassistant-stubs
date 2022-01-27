from .const import DOMAIN as DOMAIN, FroniusConfigEntryData as FroniusConfigEntryData
from homeassistant import config_entries as config_entries
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_RESOURCE as CONF_RESOURCE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any, Final

_LOGGER: Final[Any]
DHCP_REQUEST_DELAY: Final[int]
STEP_USER_DATA_SCHEMA: Any

def create_title(info: FroniusConfigEntryData) -> str: ...
async def validate_host(hass: HomeAssistant, host: str) -> tuple[str, FroniusConfigEntryData]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    info: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, conf: dict) -> FlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class CannotConnect(HomeAssistantError): ...
