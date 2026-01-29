from . import LeilSaunaConfigEntry as LeilSaunaConfigEntry
from .coordinator import LeilSaunaCoordinator as LeilSaunaCoordinator
from .entity import LeilSaunaEntity as LeilSaunaEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysaunum import SaunumData as SaunumData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LeilSaunaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SaunumData], float | int | None]

SENSORS: tuple[LeilSaunaSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LeilSaunaSensorEntity(LeilSaunaEntity, SensorEntity):
    entity_description: LeilSaunaSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LeilSaunaCoordinator, description: LeilSaunaSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
