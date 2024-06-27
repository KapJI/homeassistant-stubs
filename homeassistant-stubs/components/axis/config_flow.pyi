from . import AxisConfigEntry as AxisConfigEntry
from .const import CONF_STREAM_PROFILE as CONF_STREAM_PROFILE, CONF_VIDEO_SOURCE as CONF_VIDEO_SOURCE, DEFAULT_STREAM_PROFILE as DEFAULT_STREAM_PROFILE, DEFAULT_VIDEO_SOURCE as DEFAULT_VIDEO_SOURCE, DOMAIN as AXIS_DOMAIN
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .hub import AxisHub as AxisHub, get_axis_api as get_axis_api
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import dhcp as dhcp, ssdp as ssdp, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithConfigEntry as OptionsFlowWithConfigEntry, SOURCE_IGNORE as SOURCE_IGNORE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.typing import VolDictType as VolDictType
from homeassistant.util.network import is_link_local as is_link_local
from typing import Any

AXIS_OUI: Incomplete
DEFAULT_PORT: int
DEFAULT_PROTOCOL: str
PROTOCOL_CHOICES: Incomplete

class AxisFlowHandler(ConfigFlow, domain=AXIS_DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> AxisOptionsFlowHandler: ...
    config: Incomplete
    discovery_schema: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _create_entry(self, serial: str) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def _redo_configuration(self, entry_data: Mapping[str, Any], keep_password: bool) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _process_discovered_device(self, discovery_info: dict[str, Any]) -> ConfigFlowResult: ...

class AxisOptionsFlowHandler(OptionsFlowWithConfigEntry):
    config_entry: AxisConfigEntry
    hub: AxisHub
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_configure_stream(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
