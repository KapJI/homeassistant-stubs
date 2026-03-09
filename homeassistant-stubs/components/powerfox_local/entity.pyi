from .const import DOMAIN as DOMAIN
from .coordinator import PowerfoxLocalDataUpdateCoordinator as PowerfoxLocalDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PowerfoxLocalEntity(CoordinatorEntity[PowerfoxLocalDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PowerfoxLocalDataUpdateCoordinator) -> None: ...
