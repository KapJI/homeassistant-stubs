from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SUBSYSTEM_ADVANCED_POWER_CONTROL as SUBSYSTEM_ADVANCED_POWER_CONTROL, SUBSYSTEM_COMMON as SUBSYSTEM_COMMON, SUBSYSTEM_POWER_CONTROL as SUBSYSTEM_POWER_CONTROL, SUBSYSTEM_SITE_CONTROL as SUBSYSTEM_SITE_CONTROL
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from solaredged import SolarEdge as SolarEdge, UpdateReport
from typing import Final, override

type SolarEdgeModbusConfigEntry = ConfigEntry[SolarEdgeModbusRuntimeData]
SETTINGS_SUBSYSTEMS: Final[Incomplete]

def _merge(first: UpdateReport, second: UpdateReport) -> UpdateReport: ...

class SolarEdgeModbusDataUpdateCoordinator(DataUpdateCoordinator[UpdateReport]):
    config_entry: SolarEdgeModbusConfigEntry
    solaredge: Incomplete
    _poll: Incomplete
    _silent: set[str]
    def __init__(self, hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, solaredge: SolarEdge, *, poll: Callable[[], Awaitable[UpdateReport]], interval: timedelta, label: str) -> None: ...
    @override
    async def _async_update_data(self) -> UpdateReport: ...
    async def _async_retry(self, report: UpdateReport) -> UpdateReport: ...
    async def _async_poll(self) -> UpdateReport: ...
    def _log_silence(self, report: UpdateReport) -> None: ...

@dataclass(kw_only=True)
class SolarEdgeModbusRuntimeData:
    readings: SolarEdgeModbusDataUpdateCoordinator
    settings: SolarEdgeModbusDataUpdateCoordinator
    device_info: DeviceInfo
    inverter_device_id: str
    attachments: frozenset[str]
    @property
    def solaredge(self) -> SolarEdge: ...
    def coordinator_for(self, subsystem: str) -> SolarEdgeModbusDataUpdateCoordinator: ...
