from .const import CONF_STREAM_PROFILE as CONF_STREAM_PROFILE, CONF_VIDEO_SOURCE as CONF_VIDEO_SOURCE, DEFAULT_STREAM_PROFILE as DEFAULT_STREAM_PROFILE, DEFAULT_VIDEO_SOURCE as DEFAULT_VIDEO_SOURCE, DOMAIN as AXIS_DOMAIN
from .device import AxisNetworkDevice as AxisNetworkDevice, get_axis_device as get_axis_device
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import dhcp as dhcp, ssdp as ssdp, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IGNORE as SOURCE_IGNORE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.util.network import is_link_local as is_link_local
from typing import Any

AXIS_OUI: Incomplete
DEFAULT_PORT: int

class AxisFlowHandler(config_entries.ConfigFlow, domain=AXIS_DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> AxisOptionsFlowHandler: ...
    device_config: Incomplete
    discovery_schema: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def _create_entry(self, serial: str) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def _process_discovered_device(self, device: dict[str, Any]) -> FlowResult: ...

class AxisOptionsFlowHandler(config_entries.OptionsFlowWithConfigEntry):
    device: AxisNetworkDevice
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_configure_stream(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
