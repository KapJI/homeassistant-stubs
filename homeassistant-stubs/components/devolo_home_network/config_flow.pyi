from .const import DOMAIN as DOMAIN, PRODUCT as PRODUCT, SERIAL_NUMBER as SERIAL_NUMBER, TITLE as TITLE
from homeassistant import config_entries as config_entries, core as core
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any
STEP_USER_DATA_SCHEMA: Any

async def validate_input(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[ConfigType, None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: Union[ConfigType, None] = ...) -> FlowResult: ...
