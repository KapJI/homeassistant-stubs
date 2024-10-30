from . import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .const import DOMAIN as DOMAIN, EXECUTION_TIME_DELAY as EXECUTION_TIME_DELAY
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes, WorkArea as WorkArea
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
ERROR_ACTIVITIES: Incomplete
ERROR_STATES: Incomplete

def _check_error_free(mower_attributes: MowerAttributes) -> bool: ...
def _work_area_translation_key(work_area_id: int, key: str) -> str: ...
def handle_sending_exception(poll_after_sending: bool = False) -> Callable[[Callable[..., Awaitable[Any]]], Callable[..., Coroutine[Any, Any, None]]]: ...

class AutomowerBaseEntity(CoordinatorEntity[AutomowerDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    mower_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def mower_attributes(self) -> MowerAttributes: ...

class AutomowerAvailableEntity(AutomowerBaseEntity):
    @property
    def available(self) -> bool: ...

class AutomowerControlEntity(AutomowerAvailableEntity):
    @property
    def available(self) -> bool: ...

class WorkAreaAvailableEntity(AutomowerAvailableEntity):
    work_area_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, work_area_id: int) -> None: ...
    @property
    def work_areas(self) -> dict[int, WorkArea]: ...
    @property
    def work_area_attributes(self) -> WorkArea: ...
    @property
    def available(self) -> bool: ...

class WorkAreaControlEntity(WorkAreaAvailableEntity, AutomowerControlEntity): ...
