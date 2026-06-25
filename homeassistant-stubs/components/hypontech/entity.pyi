from .const import DOMAIN as DOMAIN
from .coordinator import HypontechDataCoordinator as HypontechDataCoordinator, HypontechPlant as HypontechPlant
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class HypontechEntity(CoordinatorEntity[HypontechDataCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HypontechDataCoordinator) -> None: ...

class HypontechPlantEntity(CoordinatorEntity[HypontechDataCoordinator]):
    _attr_has_entity_name: bool
    plant_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HypontechDataCoordinator, plant_id: str) -> None: ...
    @property
    def plant(self) -> HypontechPlant: ...
    @property
    @override
    def available(self) -> bool: ...
