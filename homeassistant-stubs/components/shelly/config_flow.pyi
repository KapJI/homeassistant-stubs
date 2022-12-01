from .const import BLEScannerMode as BLEScannerMode, BLE_MIN_VERSION as BLE_MIN_VERSION, CONF_BLE_SCANNER_MODE as CONF_BLE_SCANNER_MODE, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import get_entry_data as get_entry_data
from .utils import get_block_device_name as get_block_device_name, get_block_device_sleep_period as get_block_device_sleep_period, get_coap_context as get_coap_context, get_info_auth as get_info_auth, get_info_gen as get_info_gen, get_model_name as get_model_name, get_rpc_device_name as get_rpc_device_name, get_rpc_device_sleep_period as get_rpc_device_sleep_period, get_ws_context as get_ws_context
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import zeroconf as zeroconf
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client, selector as selector
from typing import Any, Final

HOST_SCHEMA: Final[Incomplete]
BLE_SCANNER_OPTIONS: Incomplete

async def validate_input(hass: HomeAssistant, host: str, info: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    host: str
    info: dict[str, Any]
    device_info: dict[str, Any]
    entry: Union[config_entries.ConfigEntry, None]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_credentials(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_get_info(self, host: str) -> dict[str, Any]: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> OptionsFlowHandler: ...
    @classmethod
    def async_supports_options_flow(cls, config_entry: config_entries.ConfigEntry) -> bool: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
