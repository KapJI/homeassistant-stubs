import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pypaperless import Paperless as Paperless
from pypaperless.models import Statistic, Status

type PaperlessConfigEntry = ConfigEntry[PaperlessData]
UPDATE_INTERVAL_STATISTICS: Incomplete
UPDATE_INTERVAL_STATUS: Incomplete

@dataclass
class PaperlessData:
    statistics: PaperlessStatisticCoordinator
    status: PaperlessStatusCoordinator

class PaperlessCoordinator[DataT](DataUpdateCoordinator[DataT], metaclass=abc.ABCMeta):
    config_entry: PaperlessConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: PaperlessConfigEntry, api: Paperless, name: str, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> DataT: ...
    @abstractmethod
    async def _async_update_data_internal(self) -> DataT: ...

class PaperlessStatisticCoordinator(PaperlessCoordinator[Statistic]):
    def __init__(self, hass: HomeAssistant, entry: PaperlessConfigEntry, api: Paperless) -> None: ...
    async def _async_update_data_internal(self) -> Statistic: ...

class PaperlessStatusCoordinator(PaperlessCoordinator[Status]):
    def __init__(self, hass: HomeAssistant, entry: PaperlessConfigEntry, api: Paperless) -> None: ...
    async def _async_update_data_internal(self) -> Status: ...
