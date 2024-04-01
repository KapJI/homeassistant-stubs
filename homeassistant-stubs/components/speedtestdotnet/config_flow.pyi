from .const import CONF_SERVER_ID as CONF_SERVER_ID, CONF_SERVER_NAME as CONF_SERVER_NAME, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SERVER as DEFAULT_SERVER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from typing import Any

class SpeedTestFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SpeedTestOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class SpeedTestOptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    _servers: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
