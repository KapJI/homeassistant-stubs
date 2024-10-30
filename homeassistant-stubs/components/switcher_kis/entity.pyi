from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SwitcherEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator) -> None: ...
