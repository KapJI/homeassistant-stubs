from . import AccuWeatherDataUpdateCoordinator as AccuWeatherDataUpdateCoordinator
from .const import API_IMPERIAL as API_IMPERIAL, API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_CATEGORY as ATTR_CATEGORY, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_ENGLISH as ATTR_ENGLISH, ATTR_FORECAST as ATTR_FORECAST, ATTR_LEVEL as ATTR_LEVEL, ATTR_SPEED as ATTR_SPEED, ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, MAX_FORECAST_DAYS as MAX_FORECAST_DAYS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_CUBIC_METER as CONCENTRATION_PARTS_PER_CUBIC_METER, PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfLength as UnitOfLength, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

PARALLEL_UPDATES: int

class AccuWeatherSensorDescriptionMixin:
    value_fn: Callable[[dict[str, Any], str], StateType]
    def __init__(self, value_fn) -> None: ...

class AccuWeatherSensorDescription(SensorEntityDescription, AccuWeatherSensorDescriptionMixin):
    attr_fn: Callable[[dict[str, Any]], dict[str, StateType]]
    metric_unit: Union[str, None]
    us_customary_unit: Union[str, None]
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement, attr_fn, metric_unit, us_customary_unit) -> None: ...

FORECAST_SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]
SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherSensor(CoordinatorEntity[AccuWeatherDataUpdateCoordinator], SensorEntity):
    _attr_attribution: Incomplete
    _attr_has_entity_name: bool
    entity_description: AccuWeatherSensorDescription
    _sensor_data: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _unit_system: Incomplete
    _attr_device_info: Incomplete
    forecast_day: Incomplete
    def __init__(self, coordinator: AccuWeatherDataUpdateCoordinator, description: AccuWeatherSensorDescription, forecast_day: Union[int, None] = ...) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _handle_coordinator_update(self) -> None: ...

def _get_sensor_data(sensors: dict[str, Any], kind: str, forecast_day: Union[int, None] = ...) -> Any: ...

class AccuWeatherForecastSensor(AccuWeatherSensor):
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    _sensor_data: Incomplete
    def _handle_coordinator_update(self) -> None: ...
