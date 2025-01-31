from .const import DOMAIN as DOMAIN
from .coordinator import FGLairCoordinator as FGLairCoordinator
from _typeshed import Incomplete
from ayla_iot_unofficial.fujitsu_hvac import FujitsuHVAC as FujitsuHVAC
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class FGLairEntity(CoordinatorEntity[FGLairCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FGLairCoordinator, device: FujitsuHVAC) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device(self) -> FujitsuHVAC: ...
