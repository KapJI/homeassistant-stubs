from .const import DOMAIN as DOMAIN
from .coordinator import OhmeConfigEntry as OhmeConfigEntry
from .entity import OhmeEntity as OhmeEntity, OhmeEntityDescription as OhmeEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ohme import OhmeApiClient as OhmeApiClient
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OhmeTimeDescription(OhmeEntityDescription, TimeEntityDescription):
    set_fn: Callable[[OhmeApiClient, time], Coroutine[Any, Any, bool]]
    value_fn: Callable[[OhmeApiClient], time]

TIME_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OhmeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OhmeTime(OhmeEntity, TimeEntity):
    entity_description: OhmeTimeDescription
    @property
    def native_value(self) -> time: ...
    async def async_set_value(self, value: time) -> None: ...
