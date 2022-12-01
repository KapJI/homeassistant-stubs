from . import AccuWeatherDataUpdateCoordinator as AccuWeatherDataUpdateCoordinator
from .const import API_IMPERIAL as API_IMPERIAL, API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_FORECAST as ATTR_FORECAST, CONDITION_CLASSES as CONDITION_CLASSES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.weather import ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_NATIVE_PRECIPITATION as ATTR_FORECAST_NATIVE_PRECIPITATION, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_TEMP_LOW as ATTR_FORECAST_NATIVE_TEMP_LOW, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_PRECIPITATION_PROBABILITY as ATTR_FORECAST_PRECIPITATION_PROBABILITY, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, Forecast as Forecast, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherEntity(CoordinatorEntity[AccuWeatherDataUpdateCoordinator], WeatherEntity):
    _attr_has_entity_name: bool
    _attr_native_precipitation_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_native_temperature_unit: Incomplete
    _attr_native_visibility_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _unit_system: Incomplete
    _attr_unique_id: Incomplete
    _attr_attribution: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AccuWeatherDataUpdateCoordinator) -> None: ...
    @property
    def condition(self) -> Union[str, None]: ...
    @property
    def native_temperature(self) -> float: ...
    @property
    def native_pressure(self) -> float: ...
    @property
    def humidity(self) -> int: ...
    @property
    def native_wind_speed(self) -> float: ...
    @property
    def wind_bearing(self) -> int: ...
    @property
    def native_visibility(self) -> float: ...
    @property
    def ozone(self) -> Union[int, None]: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
    @staticmethod
    def _calc_precipitation(day: dict[str, Any]) -> float: ...
