from .const import DOMAIN as DOMAIN
from .coordinator import SofarDataUpdateCoordinator as SofarDataUpdateCoordinator, SofarRuntimeData as SofarRuntimeData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

type SofarPart = tuple[str, int]
@dataclass(frozen=True, kw_only=True)
class SofarEntityDescription(EntityDescription):
    component: str
    part: SofarPart | None = ...

class SofarEntity(CoordinatorEntity[SofarDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: SofarEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, runtime_data: SofarRuntimeData, entity_description: SofarEntityDescription) -> None: ...
    def _device_info(self, runtime_data: SofarRuntimeData, serial: str) -> dr.DeviceInfo: ...
    @property
    @override
    def available(self) -> bool: ...
