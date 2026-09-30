from .coordinator import KacoDataUpdateCoordinator as KacoDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

@dataclass(frozen=True, kw_only=True)
class KacoEntityDescription(EntityDescription):
    component: str

class KacoEntity(CoordinatorEntity[KacoDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: KacoEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: KacoDataUpdateCoordinator, entity_description: KacoEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
