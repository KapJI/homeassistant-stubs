from .const import DOMAIN as DOMAIN, MIN_TIME_BETWEEN_UPDATES as MIN_TIME_BETWEEN_UPDATES
from _typeshed import Incomplete
from aiopegelonline import PegelOnline as PegelOnline, Station as Station, StationMeasurements
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type PegelOnlineConfigEntry = ConfigEntry[PegelOnlineDataUpdateCoordinator]

class PegelOnlineDataUpdateCoordinator(DataUpdateCoordinator[StationMeasurements]):
    config_entry: PegelOnlineConfigEntry
    api: Incomplete
    station: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: PegelOnlineConfigEntry, api: PegelOnline, station: Station) -> None: ...
    async def _async_update_data(self) -> StationMeasurements: ...
