from .const import MANUFACTURER as MANUFACTURER, MODEL as MODEL
from .coordinator import IronOSLiveDataCoordinator as IronOSLiveDataCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class IronOSBaseEntity(CoordinatorEntity[IronOSLiveDataCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: IronOSLiveDataCoordinator, entity_description: EntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
