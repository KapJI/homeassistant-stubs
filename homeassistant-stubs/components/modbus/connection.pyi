from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
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

def _canonical(params: ModbusParams) -> ModbusParams: ...

@dataclass
class _SharedConnection:
    params: ModbusParams
    connection: ModbusConnection
    units: dict[str, set[int]] = field(default_factory=dict)
    transient: int = ...
    @property
    def consumers(self) -> int: ...

@dataclass(frozen=True, kw_only=True)
class ModbusConnectionInfo:
    endpoint: ModbusEndpoint
    connected: bool
    units: dict[str, list[int]]

@callback
def _async_acquire(hass: HomeAssistant, params: ModbusParams, entry_id: str | None, unit_id: int) -> tuple[ModbusConnection, Callable[[], Coroutine[Any, Any, None]]]: ...
@callback
def async_get_unit(hass: HomeAssistant, entry: ConfigEntry, params: ModbusParams, unit_id: int) -> ModbusUnit: ...
@asynccontextmanager
async def async_get_temporary_unit(hass: HomeAssistant, params: ModbusParams, unit_id: int) -> AsyncIterator[ModbusUnit]: ...
@callback
def async_get_connection_info(hass: HomeAssistant) -> list[ModbusConnectionInfo]: ...
