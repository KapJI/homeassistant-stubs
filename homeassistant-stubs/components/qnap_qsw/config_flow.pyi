from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

class ConfigFlow(config_entries.ConfigFlow):
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
