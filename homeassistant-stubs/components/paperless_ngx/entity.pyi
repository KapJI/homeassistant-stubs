from .const import DOMAIN as DOMAIN
from .coordinator import PaperlessCoordinator as PaperlessCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import EntityDescription as EntityDescription
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PaperlessEntity[CoordinatorT: PaperlessCoordinator](CoordinatorEntity[CoordinatorT]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CoordinatorT, description: EntityDescription) -> None: ...
