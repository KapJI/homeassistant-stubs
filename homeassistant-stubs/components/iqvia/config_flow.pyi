from .const import CONF_ZIP_CODE as CONF_ZIP_CODE, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    data_schema: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
