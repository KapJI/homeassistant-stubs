from .const import DOMAIN as DOMAIN
from .coordinator import UnifiAccessCoordinator as UnifiAccessCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from unifi_access_api import Door as Door

class UnifiAccessEntity(CoordinatorEntity[UnifiAccessCoordinator]):
    _attr_has_entity_name: bool
    _door_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: UnifiAccessCoordinator, door: Door, key: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def _door(self) -> Door: ...

class UnifiAccessHubEntity(CoordinatorEntity[UnifiAccessCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: UnifiAccessCoordinator) -> None: ...
