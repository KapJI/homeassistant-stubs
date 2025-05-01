from .const import DOMAIN as DOMAIN
from .utils import BondHub as BondHub
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any

_LOGGER: Incomplete
USER_SCHEMA: Incomplete
DISCOVERY_SCHEMA: Incomplete
TOKEN_SCHEMA: Incomplete

async def async_get_token(hass: HomeAssistant, host: str) -> str | None: ...
async def _validate_input(hass: HomeAssistant, data: dict[str, Any]) -> tuple[str, str]: ...

class BondConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered: dict[str, str]
    def __init__(self) -> None: ...
    async def _async_try_automatic_configure(self) -> None: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_any_discovery(self, bond_id: str, host: str) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class InputValidationError(HomeAssistantError):
    base: Incomplete
    def __init__(self, base: str) -> None: ...
