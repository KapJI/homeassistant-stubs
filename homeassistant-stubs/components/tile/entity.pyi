from .const import DOMAIN as DOMAIN
from .coordinator import TileCoordinator as TileCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class TileEntity(CoordinatorEntity[TileCoordinator]):
    _attr_has_entity_name: bool
    _tile: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TileCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
