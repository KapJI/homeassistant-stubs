from .const import DOMAIN as DOMAIN
from .coordinator import IndevoltCoordinator as IndevoltCoordinator
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class IndevoltEntity(CoordinatorEntity[IndevoltCoordinator]):
    _attr_has_entity_name: bool
    @property
    def serial_number(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
