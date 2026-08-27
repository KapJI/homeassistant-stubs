from .const import DOMAIN as DOMAIN
from .coordinator import HotSpringDataUpdateCoordinator as HotSpringDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class HotSpringEntity(CoordinatorEntity[HotSpringDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HotSpringDataUpdateCoordinator, key: str) -> None: ...
