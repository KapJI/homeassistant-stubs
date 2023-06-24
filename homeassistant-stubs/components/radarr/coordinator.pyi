import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from aiopyarr import Health, RootFolder, SystemStatus
from aiopyarr.models.host_configuration import PyArrHostConfiguration as PyArrHostConfiguration
from aiopyarr.radarr_client import RadarrClient as RadarrClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Generic, TypeVar

T = TypeVar('T', bound=SystemStatus | list[RootFolder] | list[Health] | int)

class RadarrDataUpdateCoordinator(DataUpdateCoordinator[T], ABC, Generic[T], metaclass=abc.ABCMeta):
    config_entry: ConfigEntry
    api_client: Incomplete
    host_configuration: Incomplete
    def __init__(self, hass: HomeAssistant, host_configuration: PyArrHostConfiguration, api_client: RadarrClient) -> None: ...
    async def _async_update_data(self) -> T: ...
    @abstractmethod
    async def _fetch_data(self) -> T: ...

class StatusDataUpdateCoordinator(RadarrDataUpdateCoordinator[SystemStatus]):
    async def _fetch_data(self) -> SystemStatus: ...

class DiskSpaceDataUpdateCoordinator(RadarrDataUpdateCoordinator[list[RootFolder]]):
    async def _fetch_data(self) -> list[RootFolder]: ...

class HealthDataUpdateCoordinator(RadarrDataUpdateCoordinator[list[Health]]):
    async def _fetch_data(self) -> list[Health]: ...

class MoviesDataUpdateCoordinator(RadarrDataUpdateCoordinator[int]):
    async def _fetch_data(self) -> int: ...
