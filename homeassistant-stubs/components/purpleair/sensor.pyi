from .const import CONF_SENSOR_INDICES as CONF_SENSOR_INDICES
from .coordinator import PurpleAirConfigEntry as PurpleAirConfigEntry
from .entity import PurpleAirEntity as PurpleAirEntity
from _typeshed import Incomplete
from aiopurpleair.models.sensors import SensorModel as SensorModel
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

CONCENTRATION_PARTICLES_PER_100_MILLILITERS: Incomplete

@dataclass(frozen=True, kw_only=True)
class PurpleAirSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SensorModel], float | str | None]

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PurpleAirConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PurpleAirSensorEntity(PurpleAirEntity, SensorEntity):
    entity_description: PurpleAirSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, entry: PurpleAirConfigEntry, sensor_index: int, description: PurpleAirSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | str | None: ...
