from .const import DOMAIN as DOMAIN
from .coordinator import LitterRobotDataUpdateCoordinator as LitterRobotDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pylitterbot import Pet, Robot
from typing import Any, Concatenate, Generic, TypeVar

_WhiskerEntityT = TypeVar('_WhiskerEntityT', bound=Robot | Pet)

def whisker_command[_WhiskerEntityT2: LitterRobotEntity, **_P](func: Callable[Concatenate[_WhiskerEntityT2, _P], Awaitable[None]]) -> Callable[Concatenate[_WhiskerEntityT2, _P], Coroutine[Any, Any, None]]: ...
def get_device_info(whisker_entity: Robot | Pet) -> DeviceInfo: ...

class LitterRobotEntity(CoordinatorEntity[LitterRobotDataUpdateCoordinator], Generic[_WhiskerEntityT]):
    _attr_has_entity_name: bool
    robot: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, robot: _WhiskerEntityT, coordinator: LitterRobotDataUpdateCoordinator, description: EntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
