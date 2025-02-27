from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry, LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccScaleEntity as LaMarzoccScaleEntity, LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylamarzocco.const import PhysicalKey
from pylamarzocco.devices.machine import LaMarzoccoMachine as LaMarzoccoMachine

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSensorEntityDescription(LaMarzoccoEntityDescription, SensorEntityDescription):
    value_fn: Callable[[LaMarzoccoMachine], float | int]

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoKeySensorEntityDescription(LaMarzoccoEntityDescription, SensorEntityDescription):
    value_fn: Callable[[LaMarzoccoMachine, PhysicalKey], int | None]

ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]
STATISTIC_ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]
KEY_STATISTIC_ENTITIES: tuple[LaMarzoccoKeySensorEntityDescription, ...]
SCALE_ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMarzoccoSensorEntity(LaMarzoccoEntity, SensorEntity):
    entity_description: LaMarzoccoSensorEntityDescription
    @property
    def native_value(self) -> int | float | None: ...

class LaMarzoccoKeySensorEntity(LaMarzoccoEntity, SensorEntity):
    entity_description: LaMarzoccoKeySensorEntityDescription
    key: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, description: LaMarzoccoKeySensorEntityDescription, key: int) -> None: ...
    @property
    def native_value(self) -> int | None: ...

class LaMarzoccoScaleSensorEntity(LaMarzoccoSensorEntity, LaMarzoccScaleEntity):
    entity_description: LaMarzoccoSensorEntityDescription
