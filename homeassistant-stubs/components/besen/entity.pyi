from .const import NAME as NAME
from .coordinator import BesenCoordinator as BesenCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class BesenEntity(CoordinatorEntity[BesenCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_translation_key: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BesenCoordinator, key: str) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
