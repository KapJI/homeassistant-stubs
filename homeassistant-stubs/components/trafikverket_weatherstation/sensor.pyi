from .const import ATTRIBUTION as ATTRIBUTION, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN, NONE_IS_ZERO_SENSORS as NONE_IS_ZERO_SENSORS
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import as_utc as as_utc

class TrafikverketRequiredKeysMixin:
    api_key: str
    def __init__(self, api_key) -> None: ...

class TrafikverketSensorEntityDescription(SensorEntityDescription, TrafikverketRequiredKeysMixin):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: tuple[TrafikverketSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _to_datetime(measuretime: str) -> datetime: ...

class TrafikverketWeatherStation(CoordinatorEntity[TVDataUpdateCoordinator], SensorEntity):
    entity_description: TrafikverketSensorEntityDescription
    _attr_attribution: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, entry_id: str, sensor_station: str, description: TrafikverketSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
    @property
    def available(self) -> bool: ...
