from .const import CONF_ADAPTER as CONF_ADAPTER, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .util import async_get_bluetooth_adapters as async_get_bluetooth_adapters
from _typeshed import Incomplete
from homeassistant.components import onboarding as onboarding
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class BluetoothConfigFlow(ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_enable_bluetooth(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
