from .const import DOMAIN as DOMAIN
from .coordinator import WattsVisionDeviceCoordinator as WattsVisionDeviceCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from visionpluspython.models import Device as Device

class WattsVisionEntity[_T: Device](CoordinatorEntity[WattsVisionDeviceCoordinator]):
    _attr_has_entity_name: bool
    device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: WattsVisionDeviceCoordinator, device_id: str) -> None: ...
    @property
    def device(self) -> _T: ...
    @property
    def available(self) -> bool: ...
