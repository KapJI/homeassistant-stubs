from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _WhiskerEntityT as _WhiskerEntityT
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import datetime, time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Generic

@dataclass(frozen=True, kw_only=True)
class RobotTimeEntityDescription(TimeEntityDescription, Generic[_WhiskerEntityT]):
    value_fn: Callable[[_WhiskerEntityT], time | None]
    set_fn: Callable[[_WhiskerEntityT, time], Coroutine[Any, Any, bool]]

def _as_local_time(start: datetime | None) -> time | None: ...

LITTER_ROBOT_3_SLEEP_START: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LitterRobotTimeEntity(LitterRobotEntity[_WhiskerEntityT], TimeEntity):
    entity_description: RobotTimeEntityDescription[_WhiskerEntityT]
    @property
    def native_value(self) -> time | None: ...
    async def async_set_value(self, value: time) -> None: ...
