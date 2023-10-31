from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class HydrawiseEntity(CoordinatorEntity[HydrawiseDataUpdateCoordinator]):
    _attr_attribution: str
    _attr_has_entity_name: bool
    data: Incomplete
    entity_description: Incomplete
    _device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, data: dict[str, Any], coordinator: HydrawiseDataUpdateCoordinator, description: EntityDescription, device_id_key: str = ...) -> None: ...
    def _update_attrs(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
