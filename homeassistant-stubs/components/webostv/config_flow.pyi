from . import async_control_connect as async_control_connect
from .const import CONF_SOURCES as CONF_SOURCES, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from .helpers import async_get_sources as async_get_sources
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, data_entry_flow as data_entry_flow
from homeassistant.components import ssdp as ssdp
from homeassistant.const import CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Incomplete
_LOGGER: Incomplete

class FlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _host: str
    _name: str
    _uuid: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> OptionsFlowHandler: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def _async_check_configured_entry(self) -> None: ...
    async def async_step_pairing(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    options: Incomplete
    host: Incomplete
    key: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
