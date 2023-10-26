import voluptuous as vol
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from typing import Any

_LOGGER: Incomplete

def make_schema(email: str = ..., password: str = ...) -> vol.Schema: ...

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    existing_entry: ConfigEntry | None
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def _validate_and_save(self, user_input: Mapping[str, Any] | None = ..., step_id: str = ...) -> FlowResult: ...
