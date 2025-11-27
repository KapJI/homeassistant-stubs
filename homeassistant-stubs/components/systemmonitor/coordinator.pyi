import psutil_home_assistant as ha_psutil
from . import SystemMonitorConfigEntry as SystemMonitorConfigEntry
from .const import CONF_PROCESS as CONF_PROCESS, PROCESS_ERRORS as PROCESS_ERRORS
from .util import read_fan_speed as read_fan_speed
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from homeassistant.helpers.update_coordinator import TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator
from psutil import Process as Process
from psutil._common import sbattery as sbattery, sdiskusage as sdiskusage, shwtemp as shwtemp, snetio as snetio, snicaddr as snicaddr, sswap as sswap
from typing import Any, NamedTuple

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True, slots=True)
class SensorData:
    addresses: dict[str, list[snicaddr]]
    battery: sbattery | None
    boot_time: datetime
    cpu_percent: float | None
    disk_usage: dict[str, sdiskusage]
    fan_speed: dict[str, int]
    io_counters: dict[str, snetio]
    load: tuple[float, float, float]
    memory: VirtualMemory
    process_fds: dict[str, int]
    processes: list[Process]
    swap: sswap
    temperatures: dict[str, list[shwtemp]]
    def as_dict(self) -> dict[str, Any]: ...

class VirtualMemory(NamedTuple):
    total: float
    available: float
    percent: float
    used: float
    free: float

class SystemMonitorCoordinator(TimestampDataUpdateCoordinator[SensorData]):
    config_entry: SystemMonitorConfigEntry
    _psutil: Incomplete
    _arguments: Incomplete
    boot_time: datetime | None
    _initial_update: bool
    update_subscribers: dict[tuple[str, str], set[str]]
    def __init__(self, hass: HomeAssistant, config_entry: SystemMonitorConfigEntry, psutil_wrapper: ha_psutil.PsutilWrapper, arguments: list[str]) -> None: ...
    def set_subscribers_tuples(self, arguments: list[str]) -> dict[tuple[str, str], set[str]]: ...
    async def _async_update_data(self) -> SensorData: ...
    def update_data(self) -> dict[str, Any]: ...
