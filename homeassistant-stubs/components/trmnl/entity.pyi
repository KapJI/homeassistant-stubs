from .const import DOMAIN as DOMAIN
from .coordinator import TRMNLCoordinator as TRMNLCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from trmnl.models import Device as Device
from typing import Any, Concatenate

class TRMNLEntity(CoordinatorEntity[TRMNLCoordinator]):
    _attr_has_entity_name: bool
    _device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TRMNLCoordinator, device_id: int) -> None: ...
    @property
    def _device(self) -> Device: ...
    @property
    def available(self) -> bool: ...

def exception_handler[_EntityT: TRMNLEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...
