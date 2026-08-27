from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData, raise_translated_error as raise_translated_error
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from reolink_aio.api import Host as Host
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkTimeEntityDescription(TimeEntityDescription, ReolinkChannelEntityDescription):
    method: Callable[[Host, int, time], Any]
    value: Callable[[Host, int], time | None]

def _schedule_time(api: Host, ch: int, prefix: str) -> time | None: ...
def _set_start(api: Host, ch: int, value: time) -> Any: ...
def _set_end(api: Host, ch: int, value: time) -> Any: ...

TIME_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ReolinkTimeEntity(ReolinkChannelCoordinatorEntity, TimeEntity):
    entity_description: ReolinkTimeEntityDescription
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkTimeEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> time | None: ...
    @raise_translated_error
    @override
    async def async_set_value(self, value: time) -> None: ...
