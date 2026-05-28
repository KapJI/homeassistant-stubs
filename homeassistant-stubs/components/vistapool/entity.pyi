from .const import BRAND as BRAND, DOMAIN as DOMAIN, MODEL as MODEL
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class VistapoolEntity(CoordinatorEntity[VistapoolDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator) -> None: ...
    @property
    def pool_id(self) -> str: ...
    @property
    def pool_name(self) -> str: ...
    def build_unique_id(self, suffix: str) -> str: ...
