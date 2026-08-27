from .const import DOMAIN as DOMAIN
from .coordinator import LibrenmsDataUpdateCoordinator as LibrenmsDataUpdateCoordinator
from _typeshed import Incomplete
from aiolibrenms.devices.models import LibrenmsDeviceInfo as LibrenmsDeviceInfo
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class LibrenmsDeviceEntity(CoordinatorEntity[LibrenmsDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LibrenmsDataUpdateCoordinator, device_id: int) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    def _data(self) -> LibrenmsDeviceInfo: ...
