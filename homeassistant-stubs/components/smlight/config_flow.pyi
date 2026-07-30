from .bluetooth import get_ble_scanner_mode as get_ble_scanner_mode
from .const import BLEScannerMode as BLEScannerMode, CONF_BLE_SCANNER_MODE as CONF_BLE_SCANNER_MODE, DOMAIN as DOMAIN
from .coordinator import SmConfigEntry as SmConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from pysmlight import Api2
from typing import Any, override

STEP_USER_DATA_SCHEMA: Incomplete
STEP_AUTH_DATA_SCHEMA: Incomplete
BLE_SCANNER_OPTIONS: Incomplete
BLE_SCANNER_SCHEMA: Incomplete

class SmlightConfigFlow(ConfigFlow, domain=DOMAIN):
    _host: str
    _device_name: str
    client: Api2
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def _async_check_auth_required(self, user_input: dict[str, Any]) -> bool: ...
    async def _async_complete_entry(self, user_input: dict[str, Any]) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: SmConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_no_settings(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
