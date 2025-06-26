from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from airthings import Airthings as Airthings, AirthingsDevice
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

class AirthingsDataUpdateCoordinator(DataUpdateCoordinator[dict[str, AirthingsDevice]]):
    airthings: Incomplete
    def __init__(self, hass: HomeAssistant, airthings: Airthings) -> None: ...
    async def _update_method(self) -> dict[str, AirthingsDevice]: ...
