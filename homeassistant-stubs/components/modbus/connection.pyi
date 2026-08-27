from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from contextlib import asynccontextmanager
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.hass_dict import HassKey as HassKey
from modbus_connection import ModbusSerialParams, ModbusTcpParams, ModbusTlsParams, ModbusUdpParams, ModbusUnit as ModbusUnit
from modbus_connection.tmodbus import ModbusConnection
from typing import Any

_LOGGER: Incomplete
type ModbusParams = ModbusTcpParams | ModbusUdpParams | ModbusTlsParams | ModbusSerialParams
type ModbusEndpoint = tuple[str, str, int] | tuple[str, str]
DATA_MODBUS_CONNECTIONS: HassKey[dict[ModbusEndpoint, _SharedConnection]]

@dataclass
class _SharedConnection:
    params: ModbusParams
    connection: ModbusConnection
    consumers: int = ...

@callback
def _async_acquire(hass: HomeAssistant, params: ModbusParams) -> tuple[ModbusConnection, Callable[[], Coroutine[Any, Any, None]]]: ...
@callback
def async_get_unit(hass: HomeAssistant, entry: ConfigEntry, params: ModbusParams, unit_id: int) -> ModbusUnit: ...
@asynccontextmanager
async def async_get_temporary_unit(hass: HomeAssistant, params: ModbusParams, unit_id: int) -> AsyncIterator[ModbusUnit]: ...
