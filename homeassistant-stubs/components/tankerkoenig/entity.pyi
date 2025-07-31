from .coordinator import TankerkoenigDataUpdateCoordinator as TankerkoenigDataUpdateCoordinator
from _typeshed import Incomplete
from aiotankerkoenig import Station as Station
from homeassistant.const import ATTR_ID as ATTR_ID
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class TankerkoenigCoordinatorEntity(CoordinatorEntity[TankerkoenigDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TankerkoenigDataUpdateCoordinator, station: Station) -> None: ...
