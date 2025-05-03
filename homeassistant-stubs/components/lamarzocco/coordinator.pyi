import abc
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pylamarzocco import LaMarzoccoMachine as LaMarzoccoMachine

SCAN_INTERVAL: Incomplete
SETTINGS_UPDATE_INTERVAL: Incomplete
SCHEDULE_UPDATE_INTERVAL: Incomplete
STATISTICS_UPDATE_INTERVAL: Incomplete
_LOGGER: Incomplete

@dataclass
class LaMarzoccoRuntimeData:
    config_coordinator: LaMarzoccoConfigUpdateCoordinator
    settings_coordinator: LaMarzoccoSettingsUpdateCoordinator
    schedule_coordinator: LaMarzoccoScheduleUpdateCoordinator
    statistics_coordinator: LaMarzoccoStatisticsUpdateCoordinator
type LaMarzoccoConfigEntry = ConfigEntry[LaMarzoccoRuntimeData]

class LaMarzoccoUpdateCoordinator(DataUpdateCoordinator[None], metaclass=abc.ABCMeta):
    _default_update_interval = SCAN_INTERVAL
    config_entry: LaMarzoccoConfigEntry
    websocket_terminated: bool
    device: Incomplete
    def __init__(self, hass: HomeAssistant, entry: LaMarzoccoConfigEntry, device: LaMarzoccoMachine) -> None: ...
    async def _async_update_data(self) -> None: ...
    @abstractmethod
    async def _internal_async_update_data(self) -> None: ...

class LaMarzoccoConfigUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    async def _internal_async_update_data(self) -> None: ...
    websocket_terminated: bool
    async def connect_websocket(self) -> None: ...

class LaMarzoccoSettingsUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    _default_update_interval = SETTINGS_UPDATE_INTERVAL
    async def _internal_async_update_data(self) -> None: ...

class LaMarzoccoScheduleUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    _default_update_interval = SCHEDULE_UPDATE_INTERVAL
    async def _internal_async_update_data(self) -> None: ...

class LaMarzoccoStatisticsUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    _default_update_interval = STATISTICS_UPDATE_INTERVAL
    async def _internal_async_update_data(self) -> None: ...
