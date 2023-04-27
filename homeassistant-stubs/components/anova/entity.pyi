from .coordinator import AnovaCoordinator as AnovaCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AnovaEntity(CoordinatorEntity[AnovaCoordinator], Entity):
    device: Incomplete
    _attr_device_info: Incomplete
    _attr_has_entity_name: bool
    def __init__(self, coordinator: AnovaCoordinator) -> None: ...

class AnovaDescriptionEntity(AnovaEntity, Entity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AnovaCoordinator, description: EntityDescription) -> None: ...
