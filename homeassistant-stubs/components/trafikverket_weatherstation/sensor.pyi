from .const import ATTRIBUTION as ATTRIBUTION, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN, NONE_IS_ZERO_SENSORS as NONE_IS_ZERO_SENSORS
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEGREE as DEGREE, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, PERCENTAGE as PERCENTAGE, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import as_utc as as_utc, get_time_zone as get_time_zone
from typing import Any

STOCKHOLM_TIMEZONE: Any

class TrafikverketRequiredKeysMixin:
    api_key: str
    def __init__(self, api_key) -> None: ...

class TrafikverketSensorEntityDescription(SensorEntityDescription, TrafikverketRequiredKeysMixin):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_TYPES: tuple[TrafikverketSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _to_datetime(measuretime: str) -> datetime: ...

class TrafikverketWeatherStation(CoordinatorEntity[TVDataUpdateCoordinator], SensorEntity):
    entity_description: TrafikverketSensorEntityDescription
    _attr_attribution: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: TVDataUpdateCoordinator, entry_id: str, sensor_station: str, description: TrafikverketSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
    @property
    def available(self) -> bool: ...
