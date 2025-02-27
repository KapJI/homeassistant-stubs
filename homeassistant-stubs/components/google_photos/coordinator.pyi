from _typeshed import Incomplete
from google_photos_library_api.api import GooglePhotosLibraryApi as GooglePhotosLibraryApi
from google_photos_library_api.model import Album as Album
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Final

_LOGGER: Incomplete
UPDATE_INTERVAL: Final[Incomplete]
ALBUM_PAGE_SIZE: int
type GooglePhotosConfigEntry = ConfigEntry[GooglePhotosUpdateCoordinator]

class GooglePhotosUpdateCoordinator(DataUpdateCoordinator[dict[str, str]]):
    config_entry: GooglePhotosConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: GooglePhotosConfigEntry, client: GooglePhotosLibraryApi) -> None: ...
    async def _async_update_data(self) -> dict[str, str]: ...
    async def list_albums(self) -> list[Album]: ...
    async def get_or_create_album(self, album: str) -> str: ...
