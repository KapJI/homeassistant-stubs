import probatio
from . import UnifiConfigEntry as UnifiConfigEntry
from .const import CONF_ALLOW_BANDWIDTH_SENSORS as CONF_ALLOW_BANDWIDTH_SENSORS, CONF_ALLOW_UPTIME_SENSORS as CONF_ALLOW_UPTIME_SENSORS, CONF_BLOCK_CLIENT as CONF_BLOCK_CLIENT, CONF_CLIENT_SOURCE as CONF_CLIENT_SOURCE, CONF_DETECTION_TIME as CONF_DETECTION_TIME, CONF_DPI_RESTRICTIONS as CONF_DPI_RESTRICTIONS, CONF_IGNORE_LOCAL_MAC as CONF_IGNORE_LOCAL_MAC, CONF_IGNORE_WIRED_BUG as CONF_IGNORE_WIRED_BUG, CONF_MORE_OPTIONS as CONF_MORE_OPTIONS, CONF_SITE_ID as CONF_SITE_ID, CONF_SSID_FILTER as CONF_SSID_FILTER, CONF_TRACK_CLIENTS as CONF_TRACK_CLIENTS, CONF_TRACK_DEVICES as CONF_TRACK_DEVICES, CONF_TRACK_WIRED_CLIENTS as CONF_TRACK_WIRED_CLIENTS, DEFAULT_DPI_RESTRICTIONS as DEFAULT_DPI_RESTRICTIONS, DOMAIN as DOMAIN
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .hub import UnifiHub as UnifiHub, get_unifi_api as get_unifi_api
from _typeshed import Incomplete
from aiounifi.interfaces.sites import Sites as Sites
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, SectionConfig as SectionConfig, section as section
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from typing import Any, override

DEFAULT_HOST: str
DEFAULT_PORT: int
DEFAULT_SITE_ID: str
DEFAULT_VERIFY_SSL: bool

class UnifiFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    sites: Sites
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: UnifiConfigEntry) -> UnifiOptionsFlowHandler: ...
    config: dict[str, Any]
    reauth_schema: dict[probatio.Marker, Any]
    def __init__(self) -> None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_site(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> ConfigFlowResult: ...
    def _build_form_schema(self, host: str = ..., username: str = '', port: int = ..., verify_ssl: bool = ...) -> probatio.Schema: ...
    async def _async_update_sites(self, data: Mapping[str, Any]) -> Sites: ...
    @callback
    def _get_reauth_or_reconfigure_entry(self) -> ConfigEntry: ...

class UnifiOptionsFlowHandler(OptionsFlow):
    hub: UnifiHub
    options: Incomplete
    def __init__(self, config_entry: UnifiConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

async def _async_discover_unifi(hass: HomeAssistant) -> str | None: ...
def _config_from_input(user_input: dict[str, Any]) -> dict[str, Any]: ...
@contextmanager
def _catch_unifi_api_flow_errors(errors: dict[str, str]) -> Iterator[None]: ...
