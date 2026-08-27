from .const import CONF_BAUDRATE as CONF_BAUDRATE, CONF_UNIT as CONF_UNIT, DEFAULT_PORT as DEFAULT_PORT, TYPE_SERIAL as TYPE_SERIAL
from .coordinator import FlexitConfigEntry as FlexitConfigEntry, FlexitDataCoordinator as FlexitDataCoordinator
from collections.abc import Mapping
from homeassistant.components.modbus import async_get_unit as async_get_unit
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from modbus_connection import ModbusSerialParams, ModbusTcpParams
from typing import Any

_PLATFORMS: list[Platform]

def create_modbus_params(data: Mapping[str, Any]) -> ModbusSerialParams | ModbusTcpParams: ...
async def async_setup_entry(hass: HomeAssistant, entry: FlexitConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FlexitConfigEntry) -> bool: ...
