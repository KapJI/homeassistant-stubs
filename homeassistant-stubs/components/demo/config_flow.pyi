from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

CONF_STRING: str
CONF_BOOLEAN: str
CONF_INT: str
CONF_SELECT: str
CONF_MULTISELECT: str

class DemoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> OptionsFlowHandler: ...
    async def async_step_import(self, import_info: dict[str, Any]) -> FlowResult: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    options: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_options_1(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_options_2(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _update_options(self) -> FlowResult: ...
