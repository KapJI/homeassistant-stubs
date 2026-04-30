from .const import DOMAIN as DOMAIN
from .coordinator import RDWDataUpdateCoordinator as RDWDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class RDWEntity(CoordinatorEntity[RDWDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: RDWDataUpdateCoordinator) -> None: ...
