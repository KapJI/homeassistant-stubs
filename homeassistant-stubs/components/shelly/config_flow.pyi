from .const import AIOSHELLY_DEVICE_TIMEOUT_SEC as AIOSHELLY_DEVICE_TIMEOUT_SEC, DOMAIN as DOMAIN
from .utils import get_coap_context as get_coap_context, get_device_sleep_period as get_device_sleep_period
from homeassistant import config_entries as config_entries, core as core
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, HTTP_UNAUTHORIZED as HTTP_UNAUTHORIZED
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final

_LOGGER: Final[Any]
HOST_SCHEMA: Final[Any]
HTTP_CONNECT_ERRORS: Final[Any]

async def validate_input(hass: core.HomeAssistant, host: str, data: dict[str, Any]) -> dict[str, Any]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    host: str
    info: dict[str, Any]
    device_info: dict[str, Any]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_credentials(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_get_info(self, host: str) -> dict[str, Any]: ...
