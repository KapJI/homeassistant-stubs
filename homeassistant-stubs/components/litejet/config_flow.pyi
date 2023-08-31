from .const import CONF_DEFAULT_TRANSITION as CONF_DEFAULT_TRANSITION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult, FlowResultType as FlowResultType
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from typing import Any

class LiteJetOptionsFlow(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class LiteJetConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> LiteJetOptionsFlow: ...
