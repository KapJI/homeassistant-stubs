import abc
from .const import DATA_BATTERY_CAPACITY as DATA_BATTERY_CAPACITY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Generic, TypeVar
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

@dataclass
class VolvoRuntimeData:
    interval_coordinators: tuple[VolvoBaseIntervalCoordinator, ...]
type VolvoConfigEntry = ConfigEntry[VolvoRuntimeData]
type CoordinatorData = dict[str, VolvoCarsApiBaseModel | None]

def _is_invalid_api_field(field: VolvoCarsApiBaseModel | None) -> bool: ...
T = TypeVar('T', bound=dict, default=dict[str, Any])

class VolvoBaseCoordinator(DataUpdateCoordinator[T], Generic[T]):
    config_entry: VolvoConfigEntry
    context: Incomplete
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext, update_interval: timedelta | None, name: str) -> None: ...
    def get_api_field(self, api_field: str | None) -> VolvoCarsApiBaseModel | None: ...

class VolvoBaseIntervalCoordinator(VolvoBaseCoordinator[CoordinatorData], metaclass=abc.ABCMeta):
    _api_calls: list[Callable[[], Coroutine[Any, Any, Any]]]
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext, update_interval: timedelta, name: str) -> None: ...
    update_interval: Incomplete
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> CoordinatorData: ...
    @abstractmethod
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...

class VolvoVerySlowIntervalCoordinator(VolvoBaseIntervalCoordinator):
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...
    async def _async_update_data(self) -> CoordinatorData: ...

class VolvoSlowIntervalCoordinator(VolvoBaseIntervalCoordinator):
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...

class VolvoMediumIntervalCoordinator(VolvoBaseIntervalCoordinator):
    _supported_capabilities: list[str]
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...
    async def _async_get_energy_state(self) -> dict[str, VolvoCarsValueStatusField | None]: ...

class VolvoFastIntervalCoordinator(VolvoBaseIntervalCoordinator):
    def __init__(self, hass: HomeAssistant, entry: VolvoConfigEntry, context: VolvoContext) -> None: ...
    async def _async_determine_api_calls(self) -> list[Callable[[], Coroutine[Any, Any, Any]]]: ...
