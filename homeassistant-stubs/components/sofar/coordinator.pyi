from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Mapping
from dataclasses import dataclass, field
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from modbus_connection import ModbusError, ModbusTimeoutError
from propcache.api import cached_property
from sofar_modbus.model import UpdateReport
from sofar_modbus.modern.device import SofarInverter as SofarInverter
from sofar_modbus.tuning import LinkTuner as LinkTuner, TimedUnit as TimedUnit
from typing import override

_LOGGER: Incomplete

class SofarDataUpdateCoordinator(DataUpdateCoordinator[UpdateReport]):
    config_entry: SofarConfigEntry
    device: SofarInverter
    _poll: Incomplete
    _tuner: Incomplete
    _consecutive_failures: dict[str, int]
    def __init__(self, hass: HomeAssistant, entry: SofarConfigEntry, device: SofarInverter, poll: Callable[[], Awaitable[UpdateReport]], interval: timedelta, tuner: LinkTuner) -> None: ...
    @cached_property
    def device_info(self) -> dr.DeviceInfo: ...
    @override
    async def _async_update_data(self) -> UpdateReport: ...
    async def _async_observed_poll(self) -> UpdateReport: ...
    async def _retry_failed(self, report: UpdateReport) -> UpdateReport: ...

def _timed_out(failures: Mapping[str, ModbusError]) -> ModbusTimeoutError | None: ...
def _both_attempts(attempted: Mapping[str, ModbusError], retried: Mapping[str, ModbusError]) -> dict[str, ModbusError]: ...

@dataclass
class SofarRuntimeData:
    readings: SofarDataUpdateCoordinator
    settings: SofarDataUpdateCoordinator
    inverter_device_id: str
    link: TimedUnit
    tuner: LinkTuner
    wired_packs: set[int] = field(default_factory=set)
    @property
    def served_components(self) -> frozenset[str]: ...
    def pack_is_wired(self, number: int) -> bool: ...
    def coordinator_for(self, component: str) -> SofarDataUpdateCoordinator: ...
type SofarConfigEntry = ConfigEntry[SofarRuntimeData]
