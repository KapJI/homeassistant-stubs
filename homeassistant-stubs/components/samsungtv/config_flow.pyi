from .bridge import SamsungTVBridge as SamsungTVBridge, async_get_device_info as async_get_device_info, mac_from_device_info as mac_from_device_info
from .const import CONF_MANUFACTURER as CONF_MANUFACTURER, CONF_SESSION_ID as CONF_SESSION_ID, CONF_SSDP_MAIN_TV_AGENT_LOCATION as CONF_SSDP_MAIN_TV_AGENT_LOCATION, CONF_SSDP_RENDERING_CONTROL_LOCATION as CONF_SSDP_RENDERING_CONTROL_LOCATION, DEFAULT_MANUFACTURER as DEFAULT_MANUFACTURER, DOMAIN as DOMAIN, LOGGER as LOGGER, METHOD_ENCRYPTED_WEBSOCKET as METHOD_ENCRYPTED_WEBSOCKET, METHOD_LEGACY as METHOD_LEGACY, RESULT_AUTH_MISSING as RESULT_AUTH_MISSING, RESULT_CANNOT_CONNECT as RESULT_CANNOT_CONNECT, RESULT_INVALID_PIN as RESULT_INVALID_PIN, RESULT_NOT_SUPPORTED as RESULT_NOT_SUPPORTED, RESULT_SUCCESS as RESULT_SUCCESS, RESULT_UNKNOWN_HOST as RESULT_UNKNOWN_HOST, SUCCESSFUL_RESULTS as SUCCESSFUL_RESULTS, UPNP_SVC_MAIN_TV_AGENT as UPNP_SVC_MAIN_TV_AGENT, UPNP_SVC_RENDERING_CONTROL as UPNP_SVC_RENDERING_CONTROL
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import dhcp as dhcp, ssdp as ssdp, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_METHOD as CONF_METHOD, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from samsungtvws.encrypted.authenticator import SamsungTVEncryptedWSAsyncAuthenticator
from typing import Any, Self

DATA_SCHEMA: Incomplete

def _strip_uuid(udn: str) -> str: ...
def _entry_is_complete(entry: ConfigEntry, ssdp_rendering_control_location: str | None, ssdp_main_tv_agent_location: str | None) -> bool: ...
def _mac_is_same_with_incorrect_formatting(current_unformatted_mac: str, formatted_mac: str) -> bool: ...

class SamsungTVConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _host: str
    _mac: str | None
    _udn: str | None
    _upnp_udn: str | None
    _ssdp_rendering_control_location: str | None
    _ssdp_main_tv_agent_location: str | None
    _manufacturer: str | None
    _model: str | None
    _connect_result: str | None
    _method: str | None
    _name: str | None
    _title: str
    _id: int | None
    _bridge: SamsungTVBridge | None
    _device_info: dict[str, Any] | None
    _authenticator: SamsungTVEncryptedWSAsyncAuthenticator | None
    def __init__(self) -> None: ...
    def _base_config_entry(self) -> dict[str, Any]: ...
    def _get_entry_from_bridge(self) -> ConfigFlowResult: ...
    async def _async_set_device_unique_id(self, raise_on_progress: bool = True) -> None: ...
    async def _async_set_unique_id_from_udn(self, raise_on_progress: bool = True) -> None: ...
    def _async_update_and_abort_for_matching_unique_id(self) -> None: ...
    async def _async_create_bridge(self) -> None: ...
    async def _async_get_device_info_and_method(self) -> tuple[str, str | None, dict[str, Any] | None]: ...
    async def _async_get_and_check_device_info(self) -> bool: ...
    async def _async_set_name_host_from_input(self, user_input: dict[str, Any]) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pairing(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_encrypted_pairing(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _async_get_existing_matching_entry(self) -> tuple[ConfigEntry | None, bool]: ...
    def _async_update_existing_matching_entry(self) -> ConfigEntry | None: ...
    def _async_start_discovery_with_mac_address(self) -> None: ...
    def _async_abort_if_host_already_in_progress(self) -> None: ...
    def is_matching(self, other_flow: Self) -> bool: ...
    def _abort_if_manufacturer_is_not_samsung(self) -> None: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_start_encrypted_pairing(self, host: str) -> None: ...
    async def async_step_reauth_confirm_encrypted(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
