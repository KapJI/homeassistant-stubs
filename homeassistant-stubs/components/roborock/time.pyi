import datetime
from .const import DOMAIN as DOMAIN
from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockCoordinatorType as RoborockCoordinatorType, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockTimeDescription(TimeEntityDescription):
    trait: Callable[[Any], Any | None]
    get_value: Callable[[Any], datetime.time | None]
    update_value: Callable[[Any, datetime.time], Coroutine[Any, Any, None]]

TIME_DESCRIPTIONS: list[RoborockTimeDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockTimeEntity(RoborockEntityV1, TimeEntity):
    entity_description: RoborockTimeDescription
    _trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockTimeDescription, trait: Any) -> None: ...
    @property
    @override
    def native_value(self) -> time | None: ...
    @override
    async def async_set_value(self, value: time) -> None: ...
