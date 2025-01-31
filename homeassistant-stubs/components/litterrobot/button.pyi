from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import Robot as Robot
from typing import Any, Generic

@dataclass(frozen=True, kw_only=True)
class RobotButtonEntityDescription(ButtonEntityDescription, Generic[_RobotT]):
    press_fn: Callable[[_RobotT], Coroutine[Any, Any, bool]]

ROBOT_BUTTON_MAP: dict[type[Robot], RobotButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotButtonEntity(LitterRobotEntity[_RobotT], ButtonEntity):
    entity_description: RobotButtonEntityDescription[_RobotT]
    async def async_press(self) -> None: ...
