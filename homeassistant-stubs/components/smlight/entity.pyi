from .coordinator import SmBaseDataUpdateCoordinator as SmBaseDataUpdateCoordinator, base_device_info as base_device_info
from _typeshed import Incomplete
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SmEntity(CoordinatorEntity[SmBaseDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SmBaseDataUpdateCoordinator) -> None: ...
