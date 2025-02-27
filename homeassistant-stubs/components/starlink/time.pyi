from .coordinator import StarlinkConfigEntry as StarlinkConfigEntry, StarlinkData as StarlinkData, StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from datetime import time, tzinfo
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: StarlinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkTimeEntityDescription(TimeEntityDescription):
    value_fn: Callable[[StarlinkData, tzinfo], time | None]
    update_fn: Callable[[StarlinkUpdateCoordinator, time], Awaitable[None]]
    available_fn: Callable[[StarlinkData], bool]

class StarlinkTimeEntity(StarlinkEntity, TimeEntity):
    entity_description: StarlinkTimeEntityDescription
    @property
    def native_value(self) -> time | None: ...
    @property
    def available(self) -> bool: ...
    async def async_set_value(self, value: time) -> None: ...

def _utc_minutes_to_time(utc_minutes: int, timezone: tzinfo) -> time: ...
def _time_to_utc_minutes(t: time, timezone: tzinfo) -> int: ...

TIMES: Incomplete
