from .coordinator import IntelliClimaConfigEntry as IntelliClimaConfigEntry, IntelliClimaCoordinator as IntelliClimaCoordinator
from .entity import IntelliClimaECOEntity as IntelliClimaECOEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyintelliclima.intelliclima_types import IntelliClimaECO as IntelliClimaECO

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IntelliClimaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[IntelliClimaECO], int | float | str | None]

INTELLICLIMA_SENSORS: tuple[IntelliClimaSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IntelliClimaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IntelliClimaSensor(IntelliClimaECOEntity, SensorEntity):
    entity_description: IntelliClimaSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IntelliClimaCoordinator, device: IntelliClimaECO, description: IntelliClimaSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | float | str | None: ...
