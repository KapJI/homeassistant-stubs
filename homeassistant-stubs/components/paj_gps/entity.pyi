from .const import DOMAIN as DOMAIN
from .coordinator import Device as Device, PajGpsCoordinator as PajGpsCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PajGpsEntity(CoordinatorEntity[PajGpsCoordinator]):
    _attr_has_entity_name: bool
    _device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PajGpsCoordinator, device_id: int) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device(self) -> Device: ...
