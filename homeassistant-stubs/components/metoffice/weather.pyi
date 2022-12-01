from . import get_device_info as get_device_info
from .const import ATTRIBUTION as ATTRIBUTION, CONDITION_CLASSES as CONDITION_CLASSES, DOMAIN as DOMAIN, METOFFICE_COORDINATES as METOFFICE_COORDINATES, METOFFICE_DAILY_COORDINATOR as METOFFICE_DAILY_COORDINATOR, METOFFICE_HOURLY_COORDINATOR as METOFFICE_HOURLY_COORDINATOR, METOFFICE_NAME as METOFFICE_NAME, MODE_DAILY as MODE_DAILY
from .data import MetOfficeData as MetOfficeData
from _typeshed import Incomplete
from datapoint.Timestep import Timestep as Timestep
from homeassistant.components.weather import ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_NATIVE_TEMP as ATTR_FORECAST_NATIVE_TEMP, ATTR_FORECAST_NATIVE_WIND_SPEED as ATTR_FORECAST_NATIVE_WIND_SPEED, ATTR_FORECAST_PRECIPITATION_PROBABILITY as ATTR_FORECAST_PRECIPITATION_PROBABILITY, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, Forecast as Forecast, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _build_forecast_data(timestep: Timestep) -> Forecast: ...
def _get_weather_condition(metoffice_code: str) -> Union[str, None]: ...

class MetOfficeWeather(CoordinatorEntity[DataUpdateCoordinator[MetOfficeData]], WeatherEntity):
    _attr_attribution: Incomplete
    _attr_has_entity_name: bool
    _attr_native_temperature_unit: Incomplete
    _attr_native_pressure_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[MetOfficeData], hass_data: dict[str, Any], use_3hourly: bool) -> None: ...
    @property
    def condition(self) -> Union[str, None]: ...
    @property
    def native_temperature(self) -> Union[float, None]: ...
    @property
    def native_pressure(self) -> Union[float, None]: ...
    @property
    def humidity(self) -> Union[float, None]: ...
    @property
    def native_wind_speed(self) -> Union[float, None]: ...
    @property
    def wind_bearing(self) -> Union[str, None]: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
