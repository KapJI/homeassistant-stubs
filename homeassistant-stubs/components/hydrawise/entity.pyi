from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class HydrawiseEntity(CoordinatorEntity[HydrawiseDataUpdateCoordinator]):
    _attr_attribution: str
    data: Incomplete
    entity_description: Incomplete
    _attr_name: Incomplete
    def __init__(self, *, data: dict[str, Any], coordinator: HydrawiseDataUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
