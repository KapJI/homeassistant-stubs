import abc
import asyncio
from .const import DATA_BATTERY_CAPACITY as DATA_BATTERY_CAPACITY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, override
from volvocarsapi.api import VolvoCarsApi as VolvoCarsApi
from volvocarsapi.models import VolvoCarsApiBaseModel, VolvoCarsValueStatusField, VolvoCarsVehicle as VolvoCarsVehicle

VERY_SLOW_INTERVAL: int
SLOW_INTERVAL: int
MEDIUM_INTERVAL: int
FAST_INTERVAL: int
_LOGGER: Incomplete

@dataclass
class VolvoContext:
    api: VolvoCarsApi
    vehicle: VolvoCarsVehicle
    supported_commands: list[str]

@dataclass
class VolvoRuntimeData:
    fast_coordinator: VolvoFastIntervalCoordinator
    medium_coordinator: VolvoMediumIntervalCoordinator
    slow_coordinator: VolvoSlowIntervalCoordinator
    very_slow_coordinator: VolvoVerySlowIntervalCoordinator
    context: VolvoContext
    @property
    def interval_coordinators(self) -> tuple[VolvoBaseCoordinator, ...]: ...
type VolvoConfigEntry = ConfigEntry[VolvoRuntimeData]
type CoordinatorData = dict[str, VolvoCarsApiBaseModel | None]

def schedule_location_update(coordinator: VolvoBaseCoordinator) -> None: ...
def _is_invalid_api_field(field: VolvoCarsApiBaseModel | None) -> bool: ...

class VolvoBaseCoordinator(DataUpdateCoordinator[CoordinatorData], metaclass=abc.ABCMeta):
    config_entry: VolvoConfigEntry
    _api_calls: list[Callable[[], Coroutine[Any, Any, Any]]]
    context: Incomplete
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext, update_interval: timedelta, name: str) -> None: ...
    update_interval: Incomplete
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> CoordinatorData: ...
    def get_api_field(self, api_field: str | None) -> VolvoCarsApiBaseModel | None: ...
    @abstractmethod
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...

class VolvoVerySlowIntervalCoordinator(VolvoBaseCoordinator):
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    @override
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...
    @override
    async def _async_update_data(self) -> CoordinatorData: ...

class VolvoSlowIntervalCoordinator(VolvoBaseCoordinator):
    _location_supported: bool
    _location_update_task: asyncio.Task[None] | None
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    def async_schedule_location_update(self) -> None: ...
    @override
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...
    data: Incomplete
    async def _async_update_location(self) -> None: ...

class VolvoMediumIntervalCoordinator(VolvoBaseCoordinator):
    _supported_capabilities: list[str]
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    @override
    async def _async_update_data(self) -> CoordinatorData: ...
    @override
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...
    async def _async_get_energy_state(self) -> dict[str, VolvoCarsValueStatusField | None]: ...

class VolvoFastIntervalCoordinator(VolvoBaseCoordinator):
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    @override
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...
    @override
    async def _async_update_data(self) -> CoordinatorData: ...
