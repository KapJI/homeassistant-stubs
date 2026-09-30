from .const import DOMAIN as DOMAIN
from .coordinator import LibrenmsCentralDataUpdateCoordinator as LibrenmsCentralDataUpdateCoordinator
from _typeshed import Incomplete
from aiolibrenms.devices.models import LibrenmsDeviceInfo as LibrenmsDeviceInfo
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class LibrenmsDeviceEntity(CoordinatorEntity[LibrenmsCentralDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LibrenmsCentralDataUpdateCoordinator, device_id: int) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    def _data(self) -> LibrenmsDeviceInfo: ...

class LibrenmsSystemEntity(CoordinatorEntity[LibrenmsCentralDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LibrenmsCentralDataUpdateCoordinator) -> None: ...
