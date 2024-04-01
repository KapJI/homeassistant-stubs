from .const import DOMAIN as DOMAIN, FroniusConfigEntryData as FroniusConfigEntryData
from _typeshed import Incomplete
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any, Final

_LOGGER: Final[Incomplete]
DHCP_REQUEST_DELAY: Final[int]
STEP_USER_DATA_SCHEMA: Incomplete

def create_title(info: FroniusConfigEntryData) -> str: ...
async def validate_host(hass: HomeAssistant, host: str) -> tuple[str, FroniusConfigEntryData]: ...

class FroniusConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    info: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
