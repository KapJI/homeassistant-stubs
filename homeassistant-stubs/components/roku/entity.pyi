from . import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class RokuEntity(CoordinatorEntity[RokuDataUpdateCoordinator]):
    _device_id: Any
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, *, device_id: Union[str, None], coordinator: RokuDataUpdateCoordinator, description: Union[EntityDescription, None] = ...) -> None: ...
    @property
    def device_info(self) -> Union[DeviceInfo, None]: ...
