from .const import API_ATTR_OK as API_ATTR_OK, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from pyuptimerobot import UptimeRobotAccount as UptimeRobotAccount, UptimeRobotApiError as UptimeRobotApiError, UptimeRobotApiResponse as UptimeRobotApiResponse
from typing import Any

STEP_USER_DATA_SCHEMA: Any

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def _validate_input(self, data: ConfigType) -> tuple[dict[str, str], Union[UptimeRobotAccount, None]]: ...
    async def async_step_user(self, user_input: Union[ConfigType, None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, user_input: Union[ConfigType, None] = ...) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[ConfigType, None] = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: ConfigType) -> FlowResult: ...
