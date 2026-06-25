from .const import DOMAIN as DOMAIN
from .coordinator import AirVisualProCoordinator as AirVisualProCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

class AirVisualProEntity(CoordinatorEntity[AirVisualProCoordinator]):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirVisualProCoordinator, description: EntityDescription) -> None: ...
    @property
    @override
    def device_info(self) -> DeviceInfo: ...
