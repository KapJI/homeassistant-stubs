from .const import DOMAIN as DOMAIN
from .coordinator import PegelOnlineDataUpdateCoordinator as PegelOnlineDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PegelOnlineEntity(CoordinatorEntity[PegelOnlineDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    station: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PegelOnlineDataUpdateCoordinator) -> None: ...
