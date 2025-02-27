from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _WhiskerEntityT as _WhiskerEntityT
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Generic

@dataclass(frozen=True, kw_only=True)
class RobotSwitchEntityDescription(SwitchEntityDescription, Generic[_WhiskerEntityT]):
    entity_category: EntityCategory = ...
    set_fn: Callable[[_WhiskerEntityT, bool], Coroutine[Any, Any, bool]]
    value_fn: Callable[[_WhiskerEntityT], bool]

ROBOT_SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RobotSwitchEntity(LitterRobotEntity[_WhiskerEntityT], SwitchEntity):
    entity_description: RobotSwitchEntityDescription[_WhiskerEntityT]
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
