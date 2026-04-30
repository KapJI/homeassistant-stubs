from .coordinator import FreshrReadingsCoordinator as FreshrReadingsCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class FreshrEntity(CoordinatorEntity[FreshrReadingsCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FreshrReadingsCoordinator) -> None: ...
