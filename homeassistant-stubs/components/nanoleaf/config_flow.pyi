from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aionanoleaf import Nanoleaf
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import ssdp as ssdp, zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.json import save_json as save_json
from homeassistant.util.json import JsonObjectType as JsonObjectType, JsonValueType as JsonValueType, load_json_object as load_json_object
from typing import Any, Final

_LOGGER: Incomplete
CONFIG_FILE: Final[str]
USER_SCHEMA: Final[Incomplete]

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    reauth_entry: config_entries.ConfigEntry | None
    nanoleaf: Nanoleaf
    discovery_conf: JsonObjectType
    device_id: str
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def _async_homekit_zeroconf_discovery_handler(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def _async_discovery_handler(self, host: str, name: str, device_id: str) -> FlowResult: ...
    async def async_step_link(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_setup_finish(self, discovery_integration_import: bool = ...) -> FlowResult: ...
