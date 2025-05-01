from .const import DOMAIN as DOMAIN
from .coordinator import OhmeConfigEntry as OhmeConfigEntry
from .entity import OhmeEntity as OhmeEntity, OhmeEntityDescription as OhmeEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ohme import OhmeApiClient as OhmeApiClient
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OhmeNumberDescription(OhmeEntityDescription, NumberEntityDescription):
    set_fn: Callable[[OhmeApiClient, float], Coroutine[Any, Any, bool]]
    value_fn: Callable[[OhmeApiClient], float]

NUMBER_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OhmeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OhmeNumber(OhmeEntity, NumberEntity):
    entity_description: OhmeNumberDescription
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
