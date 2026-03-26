from .const import WIZ_EXCEPTIONS as WIZ_EXCEPTIONS
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pywizlight import wizlight as wizlight

_LOGGER: Incomplete
REQUEST_REFRESH_DELAY: float
type WizConfigEntry = ConfigEntry[WizData]

@dataclass
class WizData:
    coordinator: WizCoordinator
    bulb: wizlight
    scenes: list

class WizCoordinator(DataUpdateCoordinator[float | None]):
    config_entry: WizConfigEntry
    _bulb: Incomplete
    def __init__(self, hass: HomeAssistant, entry: WizConfigEntry, bulb: wizlight) -> None: ...
    async def _async_update_data(self) -> float | None: ...
