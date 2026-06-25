from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _WhiskerEntityT as _WhiskerEntityT, raise_update_failed as raise_update_failed, whisker_command as whisker_command
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import datetime, time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylitterbot import LitterRobot5, Robot as Robot
from pylitterbot.sleep_schedule import DayOfWeek, SleepScheduleDay as SleepScheduleDay
from typing import Any, Generic, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RobotTimeEntityDescription(TimeEntityDescription, Generic[_WhiskerEntityT]):
    value_fn: Callable[[_WhiskerEntityT], time | None]
    set_fn: Callable[[_WhiskerEntityT, time], Coroutine[Any, Any, bool]]

def _as_local_time(start: datetime | None) -> time | None: ...
def _lr5_schedule_day(robot: LitterRobot5, day: DayOfWeek) -> SleepScheduleDay | None: ...
def _lr5_schedule_time(robot: LitterRobot5, *, day: DayOfWeek, wake: bool) -> time | None: ...
async def _lr5_set_schedule_time(robot: LitterRobot5, value: time, *, day: DayOfWeek, wake: bool) -> bool: ...

LITTER_ROBOT_5_SLEEP_TIMES: tuple[RobotTimeEntityDescription[LitterRobot5], ...]
ROBOT_TIME_MAP: dict[type[Robot], tuple[RobotTimeEntityDescription[Any], ...]]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LitterRobotTimeEntity(LitterRobotEntity[_WhiskerEntityT], TimeEntity):
    entity_description: RobotTimeEntityDescription[_WhiskerEntityT]
    @property
    @override
    def native_value(self) -> time | None: ...
    @whisker_command
    @override
    async def async_set_value(self, value: time) -> None: ...
