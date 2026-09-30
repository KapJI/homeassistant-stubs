from .const import DOMAIN as DOMAIN
from .coordinator import IndiAllSkyConfigEntry as IndiAllSkyConfigEntry, IndiAllSkyDataUpdateCoordinator as IndiAllSkyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class IndiAllSkyEntity(CoordinatorEntity[IndiAllSkyDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: IndiAllSkyDataUpdateCoordinator, entry: IndiAllSkyConfigEntry) -> None: ...
