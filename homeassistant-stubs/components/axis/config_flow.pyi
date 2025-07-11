from . import AxisConfigEntry as AxisConfigEntry
from .const import CONF_STREAM_PROFILE as CONF_STREAM_PROFILE, CONF_VIDEO_SOURCE as CONF_VIDEO_SOURCE, DEFAULT_STREAM_PROFILE as DEFAULT_STREAM_PROFILE, DEFAULT_VIDEO_SOURCE as DEFAULT_VIDEO_SOURCE, DOMAIN as DOMAIN
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .hub import AxisHub as AxisHub, get_axis_api as get_axis_api
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_IGNORE as SOURCE_IGNORE, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.ssdp import ATTR_UPNP_FRIENDLY_NAME as ATTR_UPNP_FRIENDLY_NAME, ATTR_UPNP_PRESENTATION_URL as ATTR_UPNP_PRESENTATION_URL, ATTR_UPNP_SERIAL as ATTR_UPNP_SERIAL, SsdpServiceInfo as SsdpServiceInfo
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.helpers.typing import VolDictType as VolDictType
from homeassistant.util.network import is_link_local as is_link_local
from typing import Any

AXIS_OUI: Incomplete
DEFAULT_PORT: int
DEFAULT_PROTOCOL: str
PROTOCOL_CHOICES: Incomplete

class AxisFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> AxisOptionsFlowHandler: ...
    config: dict[str, Any]
    discovery_schema: VolDictType | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _create_entry(self, serial: str) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def _redo_configuration(self, entry_data: Mapping[str, Any], keep_password: bool) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _process_discovered_device(self, discovery_info: dict[str, Any]) -> ConfigFlowResult: ...

class AxisOptionsFlowHandler(OptionsFlow):
    config_entry: AxisConfigEntry
    hub: AxisHub
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_configure_stream(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
