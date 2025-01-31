from .const import DOMAIN as DOMAIN
from .coordinator import OverseerrCoordinator as OverseerrCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class OverseerrEntity(CoordinatorEntity[OverseerrCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: OverseerrCoordinator, key: str) -> None: ...
