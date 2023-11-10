from .const import DATA_ASUSWRT as DATA_ASUSWRT, DOMAIN as DOMAIN, KEY_COORDINATOR as KEY_COORDINATOR, KEY_SENSORS as KEY_SENSORS, SENSORS_BYTES as SENSORS_BYTES, SENSORS_CONNECTED_DEVICE as SENSORS_CONNECTED_DEVICE, SENSORS_LOAD_AVG as SENSORS_LOAD_AVG, SENSORS_RATES as SENSORS_RATES, SENSORS_TEMPERATURES as SENSORS_TEMPERATURES
from .router import AsusWrtRouter as AsusWrtRouter
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util import slugify as slugify

@dataclass
class AsusWrtSensorEntityDescription(SensorEntityDescription):
    factor: int | None = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, factor) -> None: ...

UNIT_DEVICES: str
CONNECTION_SENSORS: tuple[AsusWrtSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsusWrtSensor(CoordinatorEntity, SensorEntity):
    entity_description: AsusWrtSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, router: AsusWrtRouter, description: AsusWrtSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | str | None: ...
