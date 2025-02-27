from _typeshed import Incomplete
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type NanoleafConfigEntry = ConfigEntry[NanoleafCoordinator]

class NanoleafCoordinator(DataUpdateCoordinator[None]):
    config_entry: NanoleafConfigEntry
    nanoleaf: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: NanoleafConfigEntry, nanoleaf: Nanoleaf) -> None: ...
    async def _async_update_data(self) -> None: ...
