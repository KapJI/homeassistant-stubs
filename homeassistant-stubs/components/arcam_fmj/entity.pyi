from .coordinator import ArcamFmjCoordinator as ArcamFmjCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ArcamFmjEntity(CoordinatorEntity[ArcamFmjCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: ArcamFmjCoordinator, description: EntityDescription | None = None) -> None: ...
