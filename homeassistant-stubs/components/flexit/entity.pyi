from .coordinator import FlexitDataCoordinator as FlexitDataCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class FlexitEntity(CoordinatorEntity[FlexitDataCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FlexitDataCoordinator) -> None: ...
