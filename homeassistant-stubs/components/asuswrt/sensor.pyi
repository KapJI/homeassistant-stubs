from .const import DATA_ASUSWRT as DATA_ASUSWRT, DOMAIN as DOMAIN, SENSORS_BYTES as SENSORS_BYTES, SENSORS_CONNECTED_DEVICE as SENSORS_CONNECTED_DEVICE, SENSORS_LOAD_AVG as SENSORS_LOAD_AVG, SENSORS_RATES as SENSORS_RATES, SENSORS_TEMPERATURES as SENSORS_TEMPERATURES
from .router import AsusWrtRouter as AsusWrtRouter, KEY_COORDINATOR as KEY_COORDINATOR, KEY_SENSORS as KEY_SENSORS
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DATA_GIGABYTES as DATA_GIGABYTES, DATA_RATE_MEGABITS_PER_SECOND as DATA_RATE_MEGABITS_PER_SECOND, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class AsusWrtSensorEntityDescription(SensorEntityDescription):
    factor: Union[int, None]
    precision: int
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, factor, precision) -> None: ...

UNIT_DEVICES: str
CONNECTION_SENSORS: tuple[AsusWrtSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsusWrtSensor(CoordinatorEntity, SensorEntity):
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, router: AsusWrtRouter, description: AsusWrtSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[float, int, str, None]: ...
