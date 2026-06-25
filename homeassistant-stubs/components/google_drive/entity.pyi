from .const import DOMAIN as DOMAIN, DRIVE_FOLDER_URL_PREFIX as DRIVE_FOLDER_URL_PREFIX
from .coordinator import GoogleDriveDataUpdateCoordinator as GoogleDriveDataUpdateCoordinator
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class GoogleDriveEntity(CoordinatorEntity[GoogleDriveDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    @override
    def device_info(self) -> DeviceInfo: ...
