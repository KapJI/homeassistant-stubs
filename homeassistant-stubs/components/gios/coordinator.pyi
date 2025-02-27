from .const import API_TIMEOUT as API_TIMEOUT, DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from dataclasses import dataclass
from gios.model import GiosSensors
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type GiosConfigEntry = ConfigEntry[GiosData]

@dataclass
class GiosData:
    coordinator: GiosDataUpdateCoordinator

class GiosDataUpdateCoordinator(DataUpdateCoordinator[GiosSensors]):
    config_entry: GiosConfigEntry
    gios: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: GiosConfigEntry, session: ClientSession, station_id: int) -> None: ...
    async def _async_update_data(self) -> GiosSensors: ...
