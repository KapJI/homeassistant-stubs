from . import AccuWeatherConfigEntry as AccuWeatherConfigEntry
from .const import API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_CATEGORY as ATTR_CATEGORY, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_ENGLISH as ATTR_ENGLISH, ATTR_LEVEL as ATTR_LEVEL, ATTR_SPEED as ATTR_SPEED, ATTR_VALUE as ATTR_VALUE, MAX_FORECAST_DAYS as MAX_FORECAST_DAYS
from .coordinator import AccuWeatherDailyForecastDataUpdateCoordinator as AccuWeatherDailyForecastDataUpdateCoordinator, AccuWeatherObservationDataUpdateCoordinator as AccuWeatherObservationDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_CUBIC_METER as CONCENTRATION_PARTS_PER_CUBIC_METER, PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AccuWeatherSensorDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], str | int | float | None]
    attr_fn: Callable[[dict[str, Any]], dict[str, Any]] = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn, attr_fn) -> None: ...

FORECAST_SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]
SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AccuWeatherConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherSensor(CoordinatorEntity[AccuWeatherObservationDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: AccuWeatherSensorDescription
    _sensor_data: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AccuWeatherObservationDataUpdateCoordinator, description: AccuWeatherSensorDescription) -> None: ...
    @property
    def native_value(self) -> str | int | float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _handle_coordinator_update(self) -> None: ...
    @staticmethod
    def _get_sensor_data(sensors: dict[str, Any], kind: str) -> Any: ...

class AccuWeatherForecastSensor(CoordinatorEntity[AccuWeatherDailyForecastDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: AccuWeatherSensorDescription
    _sensor_data: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_placeholders: Incomplete
    forecast_day: Incomplete
    def __init__(self, coordinator: AccuWeatherDailyForecastDataUpdateCoordinator, description: AccuWeatherSensorDescription, forecast_day: int) -> None: ...
    @property
    def native_value(self) -> str | int | float | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _handle_coordinator_update(self) -> None: ...
    @staticmethod
    def _get_sensor_data(sensors: list[dict[str, Any]], kind: str, forecast_day: int) -> Any: ...
