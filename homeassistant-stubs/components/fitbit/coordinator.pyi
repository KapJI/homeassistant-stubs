from .api import FitbitApi as FitbitApi
from .exceptions import FitbitApiException as FitbitApiException, FitbitAuthException as FitbitAuthException
from .model import FitbitDevice as FitbitDevice
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Final

_LOGGER: Incomplete
UPDATE_INTERVAL: Final[Incomplete]
TIMEOUT: int
type FitbitConfigEntry = ConfigEntry[FitbitData]

class FitbitDeviceCoordinator(DataUpdateCoordinator[dict[str, FitbitDevice]]):
    config_entry: FitbitConfigEntry
    _api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: FitbitConfigEntry, api: FitbitApi) -> None: ...
    async def _async_update_data(self) -> dict[str, FitbitDevice]: ...

@dataclass
class FitbitData:
    api: FitbitApi
    device_coordinator: FitbitDeviceCoordinator | None
