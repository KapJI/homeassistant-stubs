from . import TRMNLConfigEntry as TRMNLConfigEntry
from .coordinator import TRMNLCoordinator as TRMNLCoordinator
from .entity import TRMNLEntity as TRMNLEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from trmnl.models import Device as Device
from typing import Any

PARALLEL_UPDATES: int

def _minutes_to_time(minutes: int) -> time: ...
def _time_to_minutes(value: time) -> int: ...

@dataclass(frozen=True, kw_only=True)
class TRMNLTimeEntityDescription(TimeEntityDescription):
    value_fn: Callable[[Device], time]
    set_value_fn: Callable[[TRMNLCoordinator, int, time], Coroutine[Any, Any, None]]

TIME_DESCRIPTIONS: tuple[TRMNLTimeEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TRMNLConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TRMNLTimeEntity(TRMNLEntity, TimeEntity):
    entity_description: TRMNLTimeEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TRMNLCoordinator, device_id: int, description: TRMNLTimeEntityDescription) -> None: ...
    @property
    def native_value(self) -> time: ...
    @exception_handler
    async def async_set_value(self, value: time) -> None: ...
