from .const import DOMAIN as DOMAIN
from .coordinator import VizioConfigEntry as VizioConfigEntry, VizioDeviceCoordinator as VizioDeviceCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class VizioEntity(CoordinatorEntity[VizioDeviceCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _device: Incomplete
    def __init__(self, config_entry: VizioConfigEntry) -> None: ...

class VizioDescriptionEntity(VizioEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: VizioConfigEntry, description: EntityDescription) -> None: ...
