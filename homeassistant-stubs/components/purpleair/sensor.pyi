from . import PurpleAirEntity as PurpleAirEntity
from .const import CONF_SENSOR_INDICES as CONF_SENSOR_INDICES, DOMAIN as DOMAIN
from .coordinator import PurpleAirDataUpdateCoordinator as PurpleAirDataUpdateCoordinator
from _typeshed import Incomplete
from aiopurpleair.models.sensors import SensorModel as SensorModel
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

CONCENTRATION_PARTICLES_PER_100_MILLILITERS: Incomplete

class PurpleAirSensorEntityDescriptionMixin:
    value_fn: Callable[[SensorModel], Union[float, str, None]]
    def __init__(self, value_fn) -> None: ...

class PurpleAirSensorEntityDescription(SensorEntityDescription, PurpleAirSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PurpleAirSensorEntity(PurpleAirEntity, SensorEntity):
    entity_description: PurpleAirSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PurpleAirDataUpdateCoordinator, entry: ConfigEntry, sensor_index: int, description: PurpleAirSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[float, str, None]: ...
