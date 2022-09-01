from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    username: str
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[Mapping[str, Any], None] = ...) -> FlowResult: ...
    async def _async_validate_input(self, user_input: Mapping[str, Any]) -> str: ...
