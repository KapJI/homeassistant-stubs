from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, PRECIPITATION_INCHES as PRECIPITATION_INCHES, SPEED_KILOMETERS_PER_HOUR as SPEED_KILOMETERS_PER_HOUR, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from lacrosse_view import Sensor

class LaCrosseSensorEntityDescriptionMixin:
    value_fn: Callable[[Sensor, str], float]
    def __init__(self, value_fn) -> None: ...

class LaCrosseSensorEntityDescription(SensorEntityDescription, LaCrosseSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

def get_value(sensor: Sensor, field: str) -> float: ...

PARALLEL_UPDATES: int
SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaCrosseViewSensor(CoordinatorEntity[DataUpdateCoordinator[list[Sensor]]], SensorEntity):
    entity_description: LaCrosseSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    index: Incomplete
    def __init__(self, description: LaCrosseSensorEntityDescription, coordinator: DataUpdateCoordinator[list[Sensor]], sensor: Sensor, index: int) -> None: ...
    @property
    def native_value(self) -> Union[float, str]: ...
