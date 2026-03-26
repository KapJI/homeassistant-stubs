from . import SimpliSafe as SimpliSafe
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

DEFAULT_SCAN_INTERVAL: Incomplete

class SimpliSafeDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    _simplisafe: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, *, name: str, simplisafe: SimpliSafe) -> None: ...
    async def _async_update_data(self) -> None: ...
