from .const import DOMAIN as DOMAIN
from .coordinator import ArcamFmjCoordinator as ArcamFmjCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

def convert_exception[**_P, _R](func: Callable[_P, Coroutine[Any, Any, _R]]) -> Callable[_P, Coroutine[Any, Any, _R]]: ...

class ArcamFmjEntity(CoordinatorEntity[ArcamFmjCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: ArcamFmjCoordinator, description: EntityDescription | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
