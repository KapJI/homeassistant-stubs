from . import async_control_connect as async_control_connect, update_client_key as update_client_key
from .const import CONF_SOURCES as CONF_SOURCES, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from .helpers import async_get_sources as async_get_sources
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from typing import Any

DATA_SCHEMA: Incomplete
_LOGGER: Incomplete

class FlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _host: str
    _name: str
    _uuid: Incomplete
    _entry: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    def _async_check_configured_entry(self) -> None: ...
    async def async_step_pairing(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class OptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    options: Incomplete
    host: Incomplete
    key: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
