from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import PoolSenseDataUpdateCoordinator as PoolSenseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PoolSenseEntity(CoordinatorEntity[PoolSenseDataUpdateCoordinator]):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PoolSenseDataUpdateCoordinator, email: str, description: EntityDescription) -> None: ...
