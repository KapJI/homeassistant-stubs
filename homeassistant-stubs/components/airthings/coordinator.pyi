from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from airthings import Airthings as Airthings, AirthingsDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
type AirthingsConfigEntry = ConfigEntry[AirthingsDataUpdateCoordinator]

class AirthingsDataUpdateCoordinator(DataUpdateCoordinator[dict[str, AirthingsDevice]]):
    airthings: Incomplete
    def __init__(self, hass: HomeAssistant, airthings: Airthings, config_entry: AirthingsConfigEntry) -> None: ...
    async def _update_method(self) -> dict[str, AirthingsDevice]: ...
