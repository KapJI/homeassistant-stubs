from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from datapoint.Forecast import Forecast
from datapoint.Manager import Manager as Manager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Literal

_LOGGER: Incomplete
type MetOfficeConfigEntry = ConfigEntry[MetOfficeRuntimeData]

@dataclass
class MetOfficeRuntimeData:
    coordinates: str
    hourly_coordinator: MetOfficeUpdateCoordinator
    daily_coordinator: MetOfficeUpdateCoordinator
    twice_daily_coordinator: MetOfficeUpdateCoordinator
    name: str

class MetOfficeUpdateCoordinator(TimestampDataUpdateCoordinator[Forecast]):
    config_entry: ConfigEntry
    _connection: Incomplete
    _latitude: Incomplete
    _longitude: Incomplete
    _frequency: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, name: str, connection: Manager, latitude: float, longitude: float, frequency: Literal['daily', 'twice-daily', 'hourly']) -> None: ...
    async def _async_update_data(self) -> Forecast: ...

def fetch_data(connection: Manager, latitude: float, longitude: float, frequency: Literal['daily', 'twice-daily', 'hourly']) -> Forecast: ...
