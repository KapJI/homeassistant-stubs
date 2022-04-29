from .const import AIOSHELLY_DEVICE_TIMEOUT_SEC as AIOSHELLY_DEVICE_TIMEOUT_SEC, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, LOGGER as LOGGER
from .utils import get_block_device_name as get_block_device_name, get_block_device_sleep_period as get_block_device_sleep_period, get_coap_context as get_coap_context, get_info_auth as get_info_auth, get_info_gen as get_info_gen, get_model_name as get_model_name, get_rpc_device_name as get_rpc_device_name
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any, Final

HOST_SCHEMA: Final[Incomplete]
HTTP_CONNECT_ERRORS: Final[Incomplete]

async def validate_input(hass: HomeAssistant, host: str, info: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    host: str
    info: dict[str, Any]
    device_info: dict[str, Any]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_credentials(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_get_info(self, host: str) -> dict[str, Any]: ...
