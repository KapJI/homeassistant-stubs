from .const import DOMAIN as DOMAIN
from .coordinator import PiHoleUpdateCoordinator as PiHoleUpdateCoordinator
from _typeshed import Incomplete
from hole import Hole as Hole
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PiHoleEntity(CoordinatorEntity[PiHoleUpdateCoordinator]):
    api: Incomplete
    _name: Incomplete
    _server_unique_id: Incomplete
    def __init__(self, api: Hole, coordinator: PiHoleUpdateCoordinator, name: str, server_unique_id: str) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
