from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator, LetPotGardenStatus as LetPotGardenStatus
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
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LetPotTimeEntityDescription[_DataT: LetPotDeviceStatus](TimeEntityDescription):
    value_fn: Callable[[_DataT], time | None]
    set_value_fn: Callable[[LetPotDeviceClient, str, time], Coroutine[Any, Any, None]]

TIME_SENSORS: tuple[LetPotTimeEntityDescription[LetPotGardenStatus], ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotTimeEntity[_DataT: LetPotDeviceStatus](LetPotEntity[_DataT], TimeEntity):
    entity_description: LetPotTimeEntityDescription[_DataT]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator[_DataT], description: LetPotTimeEntityDescription[_DataT]) -> None: ...
    @property
    @override
    def native_value(self) -> time | None: ...
    @exception_handler
    @override
    async def async_set_value(self, value: time) -> None: ...
