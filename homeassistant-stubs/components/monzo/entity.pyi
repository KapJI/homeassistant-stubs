from .const import DOMAIN as DOMAIN
from .coordinator import MonzoCoordinator as MonzoCoordinator, MonzoData as MonzoData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

class MonzoBaseEntity(CoordinatorEntity[MonzoCoordinator]):
    _attr_attribution: str
    _attr_has_entity_name: bool
    _resource_id: Incomplete
    _data_accessor: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: MonzoCoordinator, resource_id: str, device_model: str, device_name: str, data_accessor: Callable[[MonzoData], dict[str, dict[str, Any]]]) -> None: ...
    @property
    def data(self) -> dict[str, Any]: ...
    @property
    @override
    def available(self) -> bool: ...
