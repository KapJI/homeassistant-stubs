from .const import DOMAIN as DOMAIN
from .coordinator import OhmeBaseCoordinator as OhmeBaseCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from ohme import OhmeApiClient as OhmeApiClient

@dataclass(frozen=True)
class OhmeEntityDescription(EntityDescription):
    is_supported_fn: Callable[[OhmeApiClient], bool] = ...
    available_fn: Callable[[OhmeApiClient], bool] = ...

class OhmeEntity(CoordinatorEntity[OhmeBaseCoordinator]):
    _attr_has_entity_name: bool
    entity_description: OhmeEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OhmeBaseCoordinator, entity_description: OhmeEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
