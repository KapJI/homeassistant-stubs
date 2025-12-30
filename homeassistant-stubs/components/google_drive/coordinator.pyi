from .api import DriveClient as DriveClient, StorageQuotaData as StorageQuotaData
from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type GoogleDriveConfigEntry = ConfigEntry[GoogleDriveDataUpdateCoordinator]
_LOGGER: Incomplete

@dataclass
class SensorData:
    storage_quota: StorageQuotaData
    all_backups_size: int

class GoogleDriveDataUpdateCoordinator(DataUpdateCoordinator[SensorData]):
    client: DriveClient
    config_entry: GoogleDriveConfigEntry
    email_address: str
    backup_folder_id: str
    def __init__(self, hass: HomeAssistant, *, client: DriveClient, backup_folder_id: str, entry: GoogleDriveConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SensorData: ...
