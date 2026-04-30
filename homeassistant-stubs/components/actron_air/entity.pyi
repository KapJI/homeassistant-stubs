from .const import DOMAIN as DOMAIN
from .coordinator import ActronAirSystemCoordinator as ActronAirSystemCoordinator
from _typeshed import Incomplete
from actron_neo_api import ActronAirZone as ActronAirZone
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Concatenate

def actron_air_command[_EntityT: ActronAirEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...

class ActronAirEntity(CoordinatorEntity[ActronAirSystemCoordinator]):
    _attr_has_entity_name: bool
    _serial_number: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...

class ActronAirAcEntity(ActronAirEntity):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator) -> None: ...

class ActronAirZoneEntity(ActronAirEntity):
    _zone_id: int
    _zone_identifier: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator, zone: ActronAirZone) -> None: ...
