from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytile.api import API as API
from pytile.tile import Tile as Tile

type TileConfigEntry = ConfigEntry[dict[str, TileCoordinator]]
class TileCoordinator(DataUpdateCoordinator[None]):
    config_entry: TileConfigEntry
    tile: Incomplete
    client: Incomplete
    username: Incomplete
    def __init__(self, hass: HomeAssistant, entry: TileConfigEntry, client: API, tile: Tile) -> None: ...
    async def _async_update_data(self) -> None: ...
