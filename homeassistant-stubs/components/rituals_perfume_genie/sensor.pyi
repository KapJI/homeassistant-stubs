from .coordinator import RitualsConfigEntry as RitualsConfigEntry
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyrituals import Diffuser as Diffuser

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RitualsSensorEntityDescription(SensorEntityDescription):
    has_fn: Callable[[Diffuser], bool] = ...
    value_fn: Callable[[Diffuser], int | str]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RitualsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RitualsSensorEntity(DiffuserEntity, SensorEntity):
    entity_description: RitualsSensorEntityDescription
    _attr_entity_category: Incomplete
    @property
    def native_value(self) -> str | int: ...
