from .const import DOMAIN as DOMAIN
from .utils import BondHub as BondHub
from homeassistant import config_entries as config_entries, exceptions as exceptions
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, HTTP_UNAUTHORIZED as HTTP_UNAUTHORIZED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any
USER_SCHEMA: Any
DISCOVERY_SCHEMA: Any
TOKEN_SCHEMA: Any

async def _validate_input(hass: HomeAssistant, data: dict[str, Any]) -> tuple[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    _discovered: Any
    def __init__(self) -> None: ...
    async def _async_try_automatic_configure(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class InputValidationError(exceptions.HomeAssistantError):
    base: Any
    def __init__(self, base: str) -> None: ...
