from .const import DOMAIN as DOMAIN
from .coordinator import HDFuryConfigEntry as HDFuryConfigEntry
from .entity import HDFuryEntity as HDFuryEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from hdfury import HDFuryAPI as HDFuryAPI
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HDFuryNumberEntityDescription(NumberEntityDescription):
    set_value_fn: Callable[[HDFuryAPI, str], Awaitable[None]]

NUMBERS: tuple[HDFuryNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HDFuryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HDFuryNumber(HDFuryEntity, NumberEntity):
    entity_description: HDFuryNumberEntityDescription
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
