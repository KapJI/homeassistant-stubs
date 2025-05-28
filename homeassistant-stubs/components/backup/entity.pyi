from .const import DOMAIN as DOMAIN
from .coordinator import BackupDataUpdateCoordinator as BackupDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class BackupManagerBaseEntity(CoordinatorEntity[BackupDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BackupDataUpdateCoordinator) -> None: ...

class BackupManagerEntity(BackupManagerBaseEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BackupDataUpdateCoordinator, entity_description: EntityDescription) -> None: ...
