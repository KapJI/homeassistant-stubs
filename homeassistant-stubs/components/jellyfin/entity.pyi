from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import JellyfinDataT as JellyfinDataT, JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class JellyfinEntity(CoordinatorEntity[JellyfinDataUpdateCoordinator[JellyfinDataT]]):
    _attr_has_entity_name: bool
    coordinator: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: JellyfinDataUpdateCoordinator[JellyfinDataT], description: EntityDescription) -> None: ...
