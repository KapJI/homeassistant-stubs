from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SERVICE_NAME as SERVICE_NAME
from .coordinator import PyLoadCoordinator as PyLoadCoordinator
from _typeshed import Incomplete
from homeassistant.components.button import EntityDescription as EntityDescription
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class BasePyLoadEntity(CoordinatorEntity[PyLoadCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PyLoadCoordinator, entity_description: EntityDescription) -> None: ...
