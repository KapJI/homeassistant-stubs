from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry: config_entries.ConfigEntry | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
