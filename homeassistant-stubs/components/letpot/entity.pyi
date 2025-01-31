from .const import DOMAIN as DOMAIN
from .coordinator import LetPotDeviceCoordinator as LetPotDeviceCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class LetPotEntity(CoordinatorEntity[LetPotDeviceCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator) -> None: ...
