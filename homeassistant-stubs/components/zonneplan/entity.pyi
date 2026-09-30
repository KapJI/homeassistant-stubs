from .const import DOMAIN as DOMAIN
from .coordinator import ZonneplanCoordinator as ZonneplanCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ZonneplanEntity(CoordinatorEntity[ZonneplanCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ZonneplanCoordinator, entity_description: EntityDescription) -> None: ...
