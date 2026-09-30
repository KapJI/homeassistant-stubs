from .const import DOMAIN as DOMAIN
from .coordinator import VitesyDataUpdateCoordinator as VitesyDataUpdateCoordinator
from _typeshed import Incomplete
from aiovitesy.api import VitesyDevice as VitesyDevice
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class VitesyEntity(CoordinatorEntity[VitesyDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: VitesyDataUpdateCoordinator, device_id: str) -> None: ...
    @property
    def device(self) -> VitesyDevice: ...
    @property
    @override
    def available(self) -> bool: ...
