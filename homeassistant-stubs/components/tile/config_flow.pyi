import voluptuous as vol
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

STEP_REAUTH_SCHEMA: Incomplete
STEP_USER_SCHEMA: Incomplete

class TileFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _password: Incomplete
    _username: Incomplete
    def __init__(self) -> None: ...
    async def _async_verify(self, step_id: str, schema: vol.Schema) -> FlowResult: ...
    async def async_step_import(self, import_config: dict[str, Any]) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
