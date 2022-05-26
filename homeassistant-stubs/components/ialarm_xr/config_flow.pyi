from .const import DOMAIN as DOMAIN
from .utils import async_get_ialarmxr_mac as async_get_ialarmxr_mac
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, core as core
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from logging import Logger
from typing import Any

_LOGGER: Logger
DATA_SCHEMA: Incomplete

async def _async_get_device_formatted_mac(hass: core.HomeAssistant, username: str, password: str, host: str, port: int) -> str: ...

class IAlarmConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
