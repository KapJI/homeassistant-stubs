from .const import DOMAIN as DOMAIN
from .coordinator import AirGradientCoordinator as AirGradientCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Concatenate

class AirGradientEntity(CoordinatorEntity[AirGradientCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator) -> None: ...

def exception_handler[_EntityT: AirGradientEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...
