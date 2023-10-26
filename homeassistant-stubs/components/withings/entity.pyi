from .const import DOMAIN as DOMAIN
from .coordinator import WithingsDataUpdateCoordinator as WithingsDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import TypeVar

_T = TypeVar('_T', bound=WithingsDataUpdateCoordinator)

class WithingsEntity(CoordinatorEntity[_T]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _T, key: str) -> None: ...
