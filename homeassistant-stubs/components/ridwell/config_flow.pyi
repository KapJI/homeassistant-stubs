import voluptuous as vol
from .const import CALENDAR_TITLE_OPTIONS as CALENDAR_TITLE_OPTIONS, CONF_CALENDAR_TITLE as CONF_CALENDAR_TITLE, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client, selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from typing import Any

STEP_REAUTH_CONFIRM_DATA_SCHEMA: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete
OPTIONS_FLOW: Incomplete

class RidwellConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _password: str | None
    _username: str | None
    def __init__(self) -> None: ...
    async def _async_validate(self, error_step_id: str, error_schema: vol.Schema) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
