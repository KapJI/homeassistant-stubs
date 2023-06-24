from .const import CONF_SERVER_ID as CONF_SERVER_ID, CONF_SERVER_NAME as CONF_SERVER_NAME, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SERVER as DEFAULT_SERVER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class SpeedTestFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> SpeedTestOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class SpeedTestOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    _servers: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
