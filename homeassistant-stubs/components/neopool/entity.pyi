from .const import DOMAIN as DOMAIN, NAME as NAME
from .coordinator import NeoPoolCoordinator as NeoPoolCoordinator
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class NeoPoolEntity(CoordinatorEntity[NeoPoolCoordinator]):
    _attr_has_entity_name: bool
    @property
    @override
    def device_info(self) -> DeviceInfo: ...
