from .coordinator import APCUPSdCoordinator as APCUPSdCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class APCUPSdEntity(CoordinatorEntity[APCUPSdCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: APCUPSdCoordinator, description: EntityDescription) -> None: ...
