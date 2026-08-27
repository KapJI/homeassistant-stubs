from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import DOMAIN as DOMAIN, SIGNAL_NEW_POOL as SIGNAL_NEW_POOL
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
_SECONDS_PER_HOUR: int
_SECONDS_PER_MINUTE: int

@dataclass(frozen=True, kw_only=True)
class VistapoolTimeEntityDescription(TimeEntityDescription):
    value_path: str

TIME_DESCRIPTIONS: tuple[VistapoolTimeEntityDescription, ...]

def _build_time_entities(coordinator: VistapoolDataUpdateCoordinator) -> list[TimeEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VistapoolTime(VistapoolEntity, TimeEntity):
    entity_description: VistapoolTimeEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator, description: VistapoolTimeEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> time | None: ...
    @override
    async def async_set_value(self, value: time) -> None: ...
