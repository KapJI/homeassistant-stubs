from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyenphase import EnvoyData as EnvoyData
from typing import Any, Concatenate

ACTIONERRORS: Incomplete

class EnvoyBaseEntity(CoordinatorEntity[EnphaseUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    envoy_serial_num: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def data(self) -> EnvoyData: ...

def exception_handler[_EntityT: EnvoyBaseEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...
