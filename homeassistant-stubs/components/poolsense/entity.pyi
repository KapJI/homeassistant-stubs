from .const import ATTRIBUTION as ATTRIBUTION
from .coordinator import PoolSenseDataUpdateCoordinator as PoolSenseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PoolSenseEntity(CoordinatorEntity[PoolSenseDataUpdateCoordinator]):
    _attr_attribution = ATTRIBUTION
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PoolSenseDataUpdateCoordinator, email: str, description: EntityDescription) -> None: ...
