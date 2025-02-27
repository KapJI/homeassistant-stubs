from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from onedrive_personal_sdk import OneDriveClient as OneDriveClient
from onedrive_personal_sdk.models.items import Drive

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

@dataclass
class OneDriveRuntimeData:
    client: OneDriveClient
    token_function: Callable[[], Awaitable[str]]
    backup_folder_id: str
    coordinator: OneDriveUpdateCoordinator
type OneDriveConfigEntry = ConfigEntry[OneDriveRuntimeData]

class OneDriveUpdateCoordinator(DataUpdateCoordinator[Drive]):
    config_entry: OneDriveConfigEntry
    _client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: OneDriveConfigEntry, client: OneDriveClient) -> None: ...
    async def _async_update_data(self) -> Drive: ...
