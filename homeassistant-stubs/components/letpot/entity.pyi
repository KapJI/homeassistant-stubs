from .const import DOMAIN as DOMAIN
from .coordinator import LetPotDeviceCoordinator as LetPotDeviceCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Concatenate

@dataclass(frozen=True, kw_only=True)
class LetPotEntityDescription(EntityDescription):
    supported_fn: Callable[[LetPotDeviceCoordinator], bool] = ...

class LetPotEntity(CoordinatorEntity[LetPotDeviceCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator) -> None: ...

def exception_handler[_EntityT: LetPotEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...
