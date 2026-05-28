from .const import DOMAIN as DOMAIN
from .coordinator import PTDevicesCoordinator as PTDevicesCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class PTDevicesEntity(CoordinatorEntity[PTDevicesCoordinator]):
    _attr_has_entity_name: bool
    _sensor_key: Incomplete
    _device_id: Incomplete
    _user_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PTDevicesCoordinator, sensor_key: str, device_id: str) -> None: ...
    @property
    def device(self) -> dict[str, Any]: ...
    @property
    def available(self) -> bool: ...
