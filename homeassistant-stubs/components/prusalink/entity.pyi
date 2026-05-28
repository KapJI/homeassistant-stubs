from .const import DOMAIN as DOMAIN
from .coordinator import PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True, kw_only=True)
class PrusaLinkEntityDescription(EntityDescription):
    available_fn: Callable[[Any], bool] = ...
    supported_fn: Callable[[Any], bool] = ...

class PrusaLinkEntity(CoordinatorEntity[PrusaLinkUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: PrusaLinkEntityDescription
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
