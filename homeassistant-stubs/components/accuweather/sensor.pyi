from . import AccuWeatherDataUpdateCoordinator as AccuWeatherDataUpdateCoordinator
from .const import API_IMPERIAL as API_IMPERIAL, API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_FORECAST as ATTR_FORECAST, DOMAIN as DOMAIN, FORECAST_SENSOR_TYPES as FORECAST_SENSOR_TYPES, MANUFACTURER as MANUFACTURER, MAX_FORECAST_DAYS as MAX_FORECAST_DAYS, NAME as NAME, SENSOR_TYPES as SENSOR_TYPES
from .model import AccuWeatherSensorDescription as AccuWeatherSensorDescription
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherSensor(CoordinatorEntity, SensorEntity):
    _attr_attribution: Any
    coordinator: AccuWeatherDataUpdateCoordinator
    entity_description: AccuWeatherSensorDescription
    _sensor_data: Any
    _attrs: Any
    _attr_name: Any
    _attr_unique_id: Any
    _unit_system: Any
    _attr_native_unit_of_measurement: Any
    _attr_device_info: Any
    forecast_day: Any
    def __init__(self, name: str, coordinator: AccuWeatherDataUpdateCoordinator, description: AccuWeatherSensorDescription, forecast_day: Union[int, None] = ...) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _handle_coordinator_update(self) -> None: ...

def _get_sensor_data(sensors: dict[str, Any], forecast_day: Union[int, None], kind: str) -> Any: ...
