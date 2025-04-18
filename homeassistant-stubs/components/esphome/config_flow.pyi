from .const import CONF_ALLOW_SERVICE_CALLS as CONF_ALLOW_SERVICE_CALLS, CONF_DEVICE_NAME as CONF_DEVICE_NAME, CONF_NOISE_PSK as CONF_NOISE_PSK, CONF_SUBSCRIBE_LOGS as CONF_SUBSCRIBE_LOGS, DEFAULT_ALLOW_SERVICE_CALLS as DEFAULT_ALLOW_SERVICE_CALLS, DEFAULT_NEW_CONFIG_ALLOW_ALLOW_SERVICE_CALLS as DEFAULT_NEW_CONFIG_ALLOW_ALLOW_SERVICE_CALLS, DOMAIN as DOMAIN
from .dashboard import async_get_or_create_dashboard_manager as async_get_or_create_dashboard_manager, async_set_dashboard_info as async_set_dashboard_info
from _typeshed import Incomplete
from aioesphomeapi import DeviceInfo as DeviceInfo
from collections.abc import Mapping
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.hassio import HassioServiceInfo as HassioServiceInfo
from homeassistant.helpers.service_info.mqtt import MqttServiceInfo as MqttServiceInfo
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

ERROR_REQUIRES_ENCRYPTION_KEY: str
ERROR_INVALID_ENCRYPTION_KEY: str
ESPHOME_URL: str
_LOGGER: Incomplete
ZERO_NOISE_PSK: str

class EsphomeFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry: ConfigEntry
    _host: str | None
    __name: str | None
    _port: int | None
    _password: str | None
    _noise_required: bool | None
    _noise_psk: str | None
    _device_info: DeviceInfo | None
    _device_name: str | None
    def __init__(self) -> None: ...
    async def _async_step_user_base(self, user_input: dict[str, Any] | None = None, error: str | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_encryption_removed_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @property
    def _name(self) -> str: ...
    @_name.setter
    def _name(self, value: str) -> None: ...
    async def _async_try_fetch_device_info(self) -> ConfigFlowResult: ...
    async def _async_authenticate_or_add(self) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_mqtt(self, discovery_info: MqttServiceInfo) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> ConfigFlowResult: ...
    @callback
    def _async_get_entry(self) -> ConfigFlowResult: ...
    async def async_step_encryption_key(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_authenticate(self, user_input: dict[str, Any] | None = None, error: str | None = None) -> ConfigFlowResult: ...
    async def fetch_device_info(self) -> str | None: ...
    async def try_login(self) -> str | None: ...
    async def _retrieve_encryption_key_from_dashboard(self) -> bool: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
