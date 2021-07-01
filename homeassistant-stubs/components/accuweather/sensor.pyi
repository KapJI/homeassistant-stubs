from . import AccuWeatherDataUpdateCoordinator as AccuWeatherDataUpdateCoordinator
from .const import API_IMPERIAL as API_IMPERIAL, API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_ENABLED as ATTR_ENABLED, ATTR_FORECAST as ATTR_FORECAST, ATTR_LABEL as ATTR_LABEL, ATTR_UNIT_IMPERIAL as ATTR_UNIT_IMPERIAL, ATTR_UNIT_METRIC as ATTR_UNIT_METRIC, DOMAIN as DOMAIN, FORECAST_SENSOR_TYPES as FORECAST_SENSOR_TYPES, MANUFACTURER as MANUFACTURER, MAX_FORECAST_DAYS as MAX_FORECAST_DAYS, NAME as NAME, SENSOR_TYPES as SENSOR_TYPES
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ICON as ATTR_ICON, CONF_NAME as CONF_NAME, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherSensor(CoordinatorEntity, SensorEntity):
    coordinator: AccuWeatherDataUpdateCoordinator
    _sensor_data: Any
    _description: Any
    _unit_system: Any
    _name: Any
    kind: Any
    _device_class: Any
    _attrs: Any
    forecast_day: Any
    _attr_state_class: Any
    def __init__(self, name: str, kind: str, coordinator: AccuWeatherDataUpdateCoordinator, forecast_day: Union[int, None] = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def state(self) -> StateType: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    def _handle_coordinator_update(self) -> None: ...

def _get_sensor_data(sensors: dict[str, Any], forecast_day: Union[int, None], kind: str) -> Any: ...
