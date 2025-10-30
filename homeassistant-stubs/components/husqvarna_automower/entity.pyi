from . import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .const import DOMAIN as DOMAIN, EXECUTION_TIME_DELAY as EXECUTION_TIME_DELAY
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes, WorkArea as WorkArea
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Concatenate, ParamSpec, TypeVar, overload

_LOGGER: Incomplete
ERROR_ACTIVITIES: Incomplete
ERROR_STATES: Incomplete
_Entity = TypeVar('_Entity', bound='AutomowerBaseEntity')
_P = ParamSpec('_P')

@overload
def handle_sending_exception(_func: Callable[Concatenate[_Entity, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_Entity, _P], Coroutine[Any, Any, None]]: ...
@overload
def handle_sending_exception(*, poll_after_sending: bool = False) -> Callable[[Callable[Concatenate[_Entity, _P], Coroutine[Any, Any, Any]]], Callable[Concatenate[_Entity, _P], Coroutine[Any, Any, None]]]: ...
@callback
def _work_area_translation_key(work_area_id: int, key: str) -> str: ...

class AutomowerBaseEntity(CoordinatorEntity[AutomowerDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    mower_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def mower_attributes(self) -> MowerAttributes: ...
    @property
    def available(self) -> bool: ...

class AutomowerControlEntity(AutomowerBaseEntity):
    @property
    def available(self) -> bool: ...

class WorkAreaAvailableEntity(AutomowerControlEntity):
    work_area_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, work_area_id: int) -> None: ...
    @property
    def work_areas(self) -> dict[int, WorkArea]: ...
    @property
    def work_area_attributes(self) -> WorkArea: ...
    @property
    def available(self) -> bool: ...

class WorkAreaControlEntity(WorkAreaAvailableEntity, AutomowerControlEntity): ...
