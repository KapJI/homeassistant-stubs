from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator
from .entity import LetPotEntity as LetPotEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from letpot.deviceclient import LetPotDeviceClient as LetPotDeviceClient
from letpot.models import LetPotDeviceStatus as LetPotDeviceStatus
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LetPotTimeEntityDescription(TimeEntityDescription):
    value_fn: Callable[[LetPotDeviceStatus], time | None]
    set_value_fn: Callable[[LetPotDeviceClient, time], Coroutine[Any, Any, None]]

TIME_SENSORS: tuple[LetPotTimeEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotTimeEntity(LetPotEntity, TimeEntity):
    entity_description: LetPotTimeEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator, description: LetPotTimeEntityDescription) -> None: ...
    @property
    def native_value(self) -> time | None: ...
    @exception_handler
    async def async_set_value(self, value: time) -> None: ...
