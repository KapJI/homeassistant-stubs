from . import AccuWeatherDataUpdateCoordinator as AccuWeatherDataUpdateCoordinator
from .const import API_IMPERIAL as API_IMPERIAL, API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_FORECAST as ATTR_FORECAST, CONDITION_CLASSES as CONDITION_CLASSES, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, NAME as NAME
from homeassistant.components.weather import ATTR_FORECAST_CONDITION as ATTR_FORECAST_CONDITION, ATTR_FORECAST_PRECIPITATION as ATTR_FORECAST_PRECIPITATION, ATTR_FORECAST_PRECIPITATION_PROBABILITY as ATTR_FORECAST_PRECIPITATION_PROBABILITY, ATTR_FORECAST_TEMP as ATTR_FORECAST_TEMP, ATTR_FORECAST_TEMP_LOW as ATTR_FORECAST_TEMP_LOW, ATTR_FORECAST_TIME as ATTR_FORECAST_TIME, ATTR_FORECAST_WIND_BEARING as ATTR_FORECAST_WIND_BEARING, ATTR_FORECAST_WIND_SPEED as ATTR_FORECAST_WIND_SPEED, Forecast as Forecast, WeatherEntity as WeatherEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherEntity(CoordinatorEntity, WeatherEntity):
    coordinator: AccuWeatherDataUpdateCoordinator
    _unit_system: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_temperature_unit: Any
    _attr_attribution: Any
    _attr_device_info: Any
    def __init__(self, name: str, coordinator: AccuWeatherDataUpdateCoordinator) -> None: ...
    @property
    def condition(self) -> Union[str, None]: ...
    @property
    def temperature(self) -> float: ...
    @property
    def pressure(self) -> float: ...
    @property
    def humidity(self) -> int: ...
    @property
    def wind_speed(self) -> float: ...
    @property
    def wind_bearing(self) -> int: ...
    @property
    def visibility(self) -> float: ...
    @property
    def ozone(self) -> Union[int, None]: ...
    @property
    def forecast(self) -> Union[list[Forecast], None]: ...
    @staticmethod
    def _calc_precipitation(day: dict[str, Any]) -> float: ...
