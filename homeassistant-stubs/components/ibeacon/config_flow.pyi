from .const import CONF_ALLOW_NAMELESS_UUIDS as CONF_ALLOW_NAMELESS_UUIDS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import bluetooth as bluetooth
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> OptionsFlow: ...

class OptionsFlow(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict | None = None) -> FlowResult: ...
