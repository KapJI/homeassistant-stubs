from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_PORT as CONF_PORT
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

CONFIG_SCHEMA: Incomplete
SYSTEM_ID_SCHEMA: Incomplete

class ConfigFlow(config_entries.ConfigFlow):
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
