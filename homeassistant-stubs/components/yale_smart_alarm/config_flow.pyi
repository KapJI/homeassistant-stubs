from .const import CONF_AREA_ID as CONF_AREA_ID, CONF_LOCK_CODE_DIGITS as CONF_LOCK_CODE_DIGITS, DEFAULT_AREA_ID as DEFAULT_AREA_ID, DEFAULT_LOCK_CODE_DIGITS as DEFAULT_LOCK_CODE_DIGITS, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, LOGGER as LOGGER, YALE_BASE_ERRORS as YALE_BASE_ERRORS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Incomplete
DATA_SCHEMA_AUTH: Incomplete

class YaleConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    entry: ConfigEntry | None
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> YaleOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class YaleOptionsFlowHandler(OptionsFlow):
    entry: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
