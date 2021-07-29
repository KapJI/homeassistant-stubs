from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

class NotionFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    data_schema: Any
    def __init__(self) -> None: ...
    async def _show_form(self, errors: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
