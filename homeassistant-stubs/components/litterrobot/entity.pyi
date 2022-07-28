from .const import DOMAIN as DOMAIN
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from datetime import time
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from pylitterbot import Robot as Robot
from typing import Any

_P: Incomplete
_LOGGER: Incomplete
REFRESH_WAIT_TIME_SECONDS: int

class LitterRobotEntity(CoordinatorEntity[DataUpdateCoordinator[bool]]):
    robot: Incomplete
    entity_type: Incomplete
    hub: Incomplete
    def __init__(self, robot: Robot, entity_type: str, hub: LitterRobotHub) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...

class LitterRobotControlEntity(LitterRobotEntity):
    _refresh_callback: Incomplete
    def __init__(self, robot: Robot, entity_type: str, hub: LitterRobotHub) -> None: ...
    async def perform_action_and_refresh(self, action: Callable[_P, Coroutine[Any, Any, bool]], *args: _P.args, **kwargs: _P.kwargs) -> bool: ...
    async def async_call_later_callback(self, *_: Any) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def async_cancel_refresh_callback(self) -> None: ...
    @staticmethod
    def parse_time_at_default_timezone(time_str: Union[str, None]) -> Union[time, None]: ...

class LitterRobotConfigEntity(LitterRobotControlEntity):
    _attr_entity_category: Incomplete
    _assumed_state: Incomplete
    def __init__(self, robot: Robot, entity_type: str, hub: LitterRobotHub) -> None: ...
    async def perform_action_and_assume_state(self, action: Callable[[bool], Coroutine[Any, Any, bool]], assumed_state: bool) -> None: ...
