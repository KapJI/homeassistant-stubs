import probatio
from .const import CONF_BAUDRATE as CONF_BAUDRATE, CONF_UNIT_ID as CONF_UNIT_ID, DEFAULT_BAUDRATE as DEFAULT_BAUDRATE, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_UNIT_ID as DEFAULT_UNIT_ID, DOMAIN as DOMAIN, SUBSYSTEM_COMMON as SUBSYSTEM_COMMON, SUBSYSTEM_INVERTER as SUBSYSTEM_INVERTER, TYPE_SERIAL as TYPE_SERIAL, TYPE_TCP as TYPE_TCP
from .entity import inverter_name as inverter_name
from .helpers import create_modbus_params as create_modbus_params
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.modbus import async_get_temporary_unit as async_get_temporary_unit
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.data_entry_flow import section as section
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SerialPortSelector as SerialPortSelector, TextSelector as TextSelector
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from solaredged import SolarEdge
from typing import Any, override

SECTION_MORE_OPTIONS: str
MORE_OPTIONS: Incomplete
STEP_TCP: Incomplete
STEP_SERIAL: Incomplete

def _flatten(connection_type: str, user_input: dict[str, Any]) -> dict[str, Any]: ...
def _needs_relink(entry: ConfigEntry, data: Mapping[str, Any]) -> bool: ...
def _sectioned(data: Mapping[str, Any]) -> dict[str, Any]: ...
def _discovered_unit_id(discovery_info: ZeroconfServiceInfo) -> int: ...

class SolarEdgeModbusFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered: dict[str, Any]
    _discovered_title: str
    @override
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_tcp(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_serial(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_step_link(self, connection_type: str, schema: probatio.Schema, user_input: dict[str, Any] | None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_validate(self, data: dict[str, Any]) -> tuple[dict[str, str], SolarEdge | None]: ...
