import abc
from .const import CONF_OFFLINE_MODE as CONF_OFFLINE_MODE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from asyncio import Task
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pylamarzocco import LaMarzoccoMachine as LaMarzoccoMachine
from typing import Any

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
    bluetooth_coordinator: LaMarzoccoBluetoothUpdateCoordinator | None = ...
type LaMarzoccoConfigEntry = ConfigEntry[LaMarzoccoRuntimeData]

class LaMarzoccoUpdateCoordinator(DataUpdateCoordinator[None], metaclass=abc.ABCMeta):
    _default_update_interval: timedelta | None
    _ignore_offline_mode: bool
    config_entry: LaMarzoccoConfigEntry
    update_success: bool
    device: Incomplete
    _websocket_task: Task | None
    def __init__(self, hass: HomeAssistant, entry: LaMarzoccoConfigEntry, device: LaMarzoccoMachine) -> None: ...
    @property
    def websocket_terminated(self) -> bool: ...
    async def __handle_internal_update(self, func: Callable[[], Coroutine[Any, Any, None]]) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _internal_async_setup(self) -> None: ...
    @abstractmethod
    async def _internal_async_update_data(self) -> None: ...

class LaMarzoccoConfigUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    async def _internal_async_setup(self) -> None: ...
    _websocket_task: Incomplete
    async def _internal_async_update_data(self) -> None: ...
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

class LaMarzoccoBluetoothUpdateCoordinator(LaMarzoccoUpdateCoordinator):
    _ignore_offline_mode: bool
    async def _internal_async_setup(self) -> None: ...
    async def _internal_async_update_data(self) -> None: ...
