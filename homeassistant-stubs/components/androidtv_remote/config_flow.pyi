from .const import CONF_ENABLE_IME as CONF_ENABLE_IME, DOMAIN as DOMAIN
from .helpers import create_api as create_api, get_enable_ime as get_enable_ime
from _typeshed import Incomplete
from androidtvremote2 import AndroidTVRemote as AndroidTVRemote
from collections.abc import Mapping
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlowWithConfigEntry as OptionsFlowWithConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete
STEP_PAIR_DATA_SCHEMA: Incomplete

class AndroidTVRemoteConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    api: Incomplete
    reauth_entry: Incomplete
    host: Incomplete
    name: Incomplete
    mac: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def _async_start_pair(self) -> FlowResult: ...
    async def async_step_pair(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> AndroidTVRemoteOptionsFlowHandler: ...

class AndroidTVRemoteOptionsFlowHandler(OptionsFlowWithConfigEntry):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
