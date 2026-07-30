from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True)
class FroniusEntityDescription(EntityDescription):
    response_key: str | None = ...

class FroniusEntity(CoordinatorEntity['FroniusCoordinatorBase']):
    entity_description: FroniusEntityDescription
    _attr_has_entity_name: bool
    response_key: Incomplete
    solar_net_id: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: FroniusCoordinatorBase, description: FroniusEntityDescription, solar_net_id: str) -> None: ...
    def _device_data(self) -> dict[str, Any]: ...
