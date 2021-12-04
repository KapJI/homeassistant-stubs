import voluptuous as vol
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

STEP_REAUTH_CONFIRM_DATA_SCHEMA: Any
STEP_USER_DATA_SCHEMA: Any

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    _password: Any
    _username: Any
    def __init__(self) -> None: ...
    async def _async_validate(self, error_step_id: str, error_schema: vol.Schema) -> FlowResult: ...
    async def async_step_reauth(self, config: ConfigType) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
