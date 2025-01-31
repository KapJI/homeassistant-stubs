from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry, LitterRobotDataUpdateCoordinator as LitterRobotDataUpdateCoordinator
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import Robot as Robot
from typing import Any, Generic, TypeVar

_CastTypeT = TypeVar('_CastTypeT', int, float, str)

@dataclass(frozen=True, kw_only=True)
class RobotSelectEntityDescription(SelectEntityDescription, Generic[_RobotT, _CastTypeT]):
    entity_category: EntityCategory = ...
    current_fn: Callable[[_RobotT], _CastTypeT | None]
    options_fn: Callable[[_RobotT], list[_CastTypeT]]
    select_fn: Callable[[_RobotT, str], Coroutine[Any, Any, bool]]

ROBOT_SELECT_MAP: dict[type[Robot], RobotSelectEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotSelectEntity(LitterRobotEntity[_RobotT], SelectEntity, Generic[_RobotT, _CastTypeT]):
    entity_description: RobotSelectEntityDescription[_RobotT, _CastTypeT]
    _attr_options: Incomplete
    def __init__(self, robot: _RobotT, coordinator: LitterRobotDataUpdateCoordinator, description: RobotSelectEntityDescription[_RobotT, _CastTypeT]) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
