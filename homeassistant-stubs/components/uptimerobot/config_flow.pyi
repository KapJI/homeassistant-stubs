from .const import API_ATTR_OK as API_ATTR_OK, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from pyuptimerobot import UptimeRobotAccount as UptimeRobotAccount, UptimeRobotApiError as UptimeRobotApiError, UptimeRobotApiResponse as UptimeRobotApiResponse
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def _validate_input(self, data: dict[str, Any]) -> tuple[dict[str, str], UptimeRobotAccount | None]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
